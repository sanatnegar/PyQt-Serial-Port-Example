int led = 13;                       // On Board LED
int AI0, AI1, AI2, AI3, AI4, AI5;
String sDPINS;
String sPWM;
int iPWM;
String inputString = "";            // a String to hold incoming data
bool stringComplete = false;        // whether the string is complete

void setup() {
  Serial.begin(115200);
  pinMode(led, OUTPUT);
}

void loop() {

  readAnalogs();
  delay(250);

  if (stringComplete) {
    sPWM = inputString;
    inputString = "";
    stringComplete = false;
    iPWM = sPWM.toInt();
    analogWrite(led, iPWM);
  }
}

void readAnalogs() {

  AI0 = analogRead(A0);
  AI1 = analogRead(A1);
  AI2 = analogRead(A2);
  AI3 = analogRead(A3);
  AI4 = analogRead(A4);
  AI5 = analogRead(A5);

  Serial.print("#");
  Serial.print(String(AI0));
  Serial.print(",");
  Serial.print(String(AI1));
  Serial.print(",");
  Serial.print(String(AI2));
  Serial.print(",");
  Serial.print(String(AI3));
  Serial.print(",");
  Serial.print(String(AI4));
  Serial.print(",");
  Serial.print(String(AI5));
  Serial.println("|");
}

void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag so the main loop can
    // do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    }
  }
}
