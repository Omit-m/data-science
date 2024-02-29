
#include <Wire.h> 
#include <LiquidCrystal_I2C.h> 
#include <Keypad.h> 
LiquidCrystal_I2C lcd(0x27, 16, 2); 
const int relayModule = 5;         
const int flameSensorPin = A0; 
const int ledPin = 3; 
unsigned int SetPoint = 0;        
unsigned long fillingTime = 0;   
unsigned long startTime = 0;       
bool filling = false; 
const byte ROWS = 4; // Four rows 
const byte COLS = 4; // Four columns 
char keys[ROWS][COLS] = { 
  {'1', '2', '3', 'A'}, 
  {'4', '5', '6', 'B'}, 
  {'7', '8', '9', 'C'}, 
  {'*', '0', '#', 'D'} 
}; 
byte rowPins[ROWS] = {13, 12, 11, 10};    // Connect to the row pinouts of 
the keypad 
byte colPins[COLS] = {9, 8, 7, 6}; // Connect to the column pinouts of the 
keypad 
Keypad keypad = Keypad(makeKeymap(keys), rowPins, colPins, ROWS, COLS); 
void setup() { 
  lcd.begin(); 
  Serial.begin(9600); 
  lcd.backlight(); 
  pinMode(relayModule, OUTPUT); 
  digitalWrite(relayModule, HIGH);  
  pinMode(4, OUTPUT); 
  digitalWrite(4, HIGH); 
  pinMode(flameSensorPin, INPUT); 
  pinMode(ledPin, OUTPUT); 
  message(); 
} 
void loop() { 
  flame(); 
  char key = keypad.getKey(); 
  if (key) { 
    handleKeypadInput(key); 
  } 
 
  if (filling && (millis() - startTime) > fillingTime) { 
    stopFilling(); 
  } 
} 
void handleKeypadInput(char key) { 
  if (key == 'A') { 
    // 'A' key on the keypad pressed, set the desired amount of water to be 
filled 
    flame(); 
    lcd.clear(); 
    lcd.setCursor(0, 0); 
    lcd.print("Enter Amount(mL)"); 
    lcd.setCursor(5, 1); 
    String amountStr = ""; 
    char keyInput = 0; 
    while (keyInput != '#') { 
      flame(); 
      keyInput = keypad.getKey(); 
      if (keyInput) { 
        lcd.print(keyInput); 
        amountStr += keyInput; 
      } 
    } 
    SetPoint = amountStr.toInt(); 
    fillingTime= SetPoint*20; 
    if (SetPoint > 2000) { 
      lcd.clear(); 
      lcd.print("Limit Crossed"); 
      delay(2000); 
      lcd.clear(); 
      flame(); 
      message(); 
      return; 
    } 
    lcd.clear(); 
    lcd.print("Amount Set:"); 
    lcd.print(SetPoint); 
    delay(1000); 
  } 
  else if (key == 'D') { 
    // 'D' key on the keypad pressed, start the filling process 
    if (SetPoint <= 0) { 
      lcd.clear(); 
      lcd.setCursor(2, 0); 
      lcd.print("Enter Amount"); 
      lcd.setCursor(5, 1); 
      lcd.print("First"); 
      delay(2000); 
      lcd.clear(); 
      flame(); 
      message(); 
      return; 
    } 
    startFilling(); 
  } 
} 
void startFilling() { 
  filling = true; 
  startTime = millis(); 
  digitalWrite(relayModule, LOW); // Activate relay to start the water flow 
  lcd.clear(); 
  lcd.print("Filling..."); 
  flame(); 
} 
void stopFilling() { 
  filling = false; 
  digitalWrite(relayModule, HIGH); // Deactivate relay to stop the water 
flow 
  lcd.clear(); 
  lcd.print("Filling Complete"); 
  delay(2000); 
  lcd.clear(); 
  message(); 
  flame(); 
} 
void message() { 
  lcd.clear(); 
  lcd.setCursor(0, 0); 
  lcd.print("Put the bottle &"); 
  lcd.setCursor(0, 1); 
  lcd.print("Press A to start"); 
  delay(3000); 
} 
void flame() { 
  int flameValue = digitalRead(flameSensorPin); 
  if (flameValue == LOW)  
  { 
    digitalWrite(ledPin, HIGH); 
    delay(1000); 
    digitalWrite(ledPin, LOW); 
    delay(1000); 
  } 
}

