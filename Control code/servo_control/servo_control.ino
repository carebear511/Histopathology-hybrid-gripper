#include <Servo.h>
Servo myservo; 
String inByte;
int pos;
String pos2;
int i;


void setup() {
 
  myservo.attach(10);
  Serial.begin(9600);
  myservo.write(50);   
  i = 50;
}

void loop()
{    
  if (Serial.available() > 0) {
    inByte = Serial.readStringUntil('\n'); // read data until newline
    pos = inByte.toInt();   // change datatype from string to integer   

    while (i != pos) {
    if (i<=pos){
      myservo.write(i);
      delay(50);
      i = i+1;
    }
    else {
      myservo.write(i);
      delay(50);
      i = i-1;
    }
    }

    myservo.write(pos);
    i = pos;

    delay(100);

//    Serial.println(inByte);
    Serial.print("Servo in position: ");  
    Serial.println(myservo.read());
  }

}
