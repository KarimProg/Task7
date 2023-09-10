/*
 * File: cytron_cleaner.ino
 * Author: Group 6
 * Description: This program passes motor speed through an exponential smoothing filter
 *              to provide the motor with a soft start. (Input pin could be pulled down
 *              for more stable results)
 * Date: [8/9/2023]
 */

/* Macros */
#define DIR 4
#define PWM 3
#define input A0

uint8_t mtrspd = 0;  // Motor speed to reach

float alpha = 0.3;  // Smoothing factor
float output = 0;   // Output of filter

void setup() {
  // Begin serial communication at default rate (9600)
  Serial.begin(9600);

  // Pin setup
  pinMode(DIR, OUTPUT);
  pinMode(PWM, OUTPUT);
  pinMode(input, INPUT);

  // Motor direction
  digitalWrite(DIR, LOW);
}

void loop() {
  // Take input (e.g. potentiometer)
  mtrspd = map(analogRead(input), 0, 1023, 0, 255);

  // Exponential smoothing eqn
  output = alpha * mtrspd + (1 - alpha) * output;

  // Monitor output
  Serial.println("PWM: ");
  Serial.println(output);

  // Motor speed output
  analogWrite(PWM, int(output));

  delay(100);
}