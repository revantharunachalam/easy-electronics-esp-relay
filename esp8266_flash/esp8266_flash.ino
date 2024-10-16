#define RELAY1 D0
#define RELAY2 D1
#define RELAY3 D2
#define RELAY4 D3
#define RELAY5 D4
#define RELAY6 D5
#define RELAY7 D6
#define RELAY8 D7
#define RELAY9 D8

String control;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(RELAY1, OUTPUT);
  pinMode(RELAY2, OUTPUT);
  pinMode(RELAY3, OUTPUT);
  pinMode(RELAY4, OUTPUT);
  pinMode(RELAY5, OUTPUT);
  pinMode(RELAY6, OUTPUT);
  pinMode(RELAY7, OUTPUT);
  pinMode(RELAY8, OUTPUT);
  pinMode(RELAY9, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  while (Serial.available() > 0) {
    control = Serial.readStringUntil('\n'); 

    // Relay 1
    if(control == "RELAY1 ON") {
      digitalWrite(RELAY1, HIGH);
      delay(500);
    }
    else if(control == "RELAY1 OFF") {
      digitalWrite(RELAY1, LOW);
      delay(500);
    }

    // Relay 2
    else if(control == "RELAY2 ON") {
      digitalWrite(RELAY2, HIGH);
      delay(500);
    }
    else if(control == "RELAY2 OFF") {
      digitalWrite(RELAY2, LOW);
      delay(500);
    }

    // Relay 3
    else if(control == "RELAY3 ON") {
      digitalWrite(RELAY3, HIGH);
      delay(500);
    }
    else if(control == "RELAY3 OFF") {
      digitalWrite(RELAY3, LOW);
      delay(500);
    }

    // Relay 4
    else if(control == "RELAY4 ON") {
      digitalWrite(RELAY4, HIGH);
      delay(500);
    }
    else if(control == "RELAY4 OFF") {
      digitalWrite(RELAY4, LOW);
      delay(500);
    }

    // Relay 5
    else if(control == "RELAY5 ON") {
      digitalWrite(RELAY5, HIGH);
      delay(500);
    }
    else if(control == "RELAY5 OFF") {
      digitalWrite(RELAY5, LOW);
      delay(500);
    }

    // Relay 6
    else if(control == "RELAY6 ON") {
      digitalWrite(RELAY6, HIGH);
      delay(500);
    }
    else if(control == "RELAY6 OFF") {
      digitalWrite(RELAY6, LOW);
      delay(500);
    }

    // Relay 7
    else if(control == "RELAY7 ON") {
      digitalWrite(RELAY7, HIGH);
      delay(500);
    }
    else if(control == "RELAY7 OFF") {
      digitalWrite(RELAY7, LOW);
      delay(500);
    }

    // Relay 8
    else if(control == "RELAY8 ON") {
      digitalWrite(RELAY8, HIGH);
      delay(500);
    }
    else if(control == "RELAY8 OFF") {
      digitalWrite(RELAY8, LOW);
      delay(500);
    }

    // Relay 9
    else if(control == "RELAY9 ON") {
      digitalWrite(RELAY9, HIGH);
      delay(500);
    }
    else if(control == "RELAY9 OFF") {
      digitalWrite(RELAY9, LOW);
      delay(500);
    }
    
  }
}
