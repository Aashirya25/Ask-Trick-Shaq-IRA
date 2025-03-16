#include <Servo.h> 

// Servo setup
Servo myServo1;
Servo myServo2;

// Variables
bool btn = false;
bool activate = true;
int result;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(13, OUTPUT);
  pinMode(2, INPUT);
  myServo1.attach(3);
  myServo2.attach(4);
}

void loop() {
  btn = digitalRead(2);
  result = Serial.parseInt();
  if (length(result) or !btn) {
    digitalWrite(13, HIGH);
    myServo1.write(90);
    delay(250);
    myServo2.write(-90);
    myServo1.write(-90);
    delay(1000);
    myServo2.write(90);
    delay(250);
  }
}
