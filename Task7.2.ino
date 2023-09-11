#include <PID_v1.h>

#define FLOW_SENSOR_PIN 2
#define MOTOR_PIN 3

volatile int pulseCount = 0;
float flowRate = 0;
int motorSpeed = 0;

// Define PID tuning parameters
double Kp = 1;
double Ki = 0.1;
double Kd = 0.01;

// Define setpoint and input variables
double setpoint = 90;
double input = 0;

// Define output variable
double output = 0;

// Create PID controller object
PID myPID(&input, &output, &setpoint, Kp, Ki, Kd, DIRECT);

void setup() {
  // Initialize flow meter and motor
  pinMode(FLOW_SENSOR_PIN, INPUT_PULLUP);
  pinMode(MOTOR_PIN, OUTPUT);
  digitalWrite(MOTOR_PIN, LOW);
  attachInterrupt(digitalPinToInterrupt(FLOW_SENSOR_PIN), pulseCounter, RISING);
  Serial.begin(9600);
}

void loop() {
  // Calculate flow rate and update motor speed accordingly
  flowRate = pulseCount * 2.25; // Convert pulses per second to L/min
  motorSpeed = map(flowRate, 0, 10, 0, 255);
  analogWrite(MOTOR_PIN, motorSpeed);

  // Print flow rate and motor speed to serial monitor
  Serial.print("Flow rate: ");
  Serial.print(flowRate);
  Serial.print(" L/min\tMotor speed: ");
  Serial.println(motorSpeed);

  pulseCount = 0; // Reset pulse count for next measurement
  delay(1000);
  // Read flow rate from flow meter
  input = readFlowRate();

  // Compute PID output
  myPID.Compute();

  // Adjust motor speed based on PID output
  adjustMotorSpeed(output);

  // Wait for some time before repeating the loop
  delay(100);
}

// Read flow rate from flow meter and return the value
double readFlowRate() {
  // Count pulses for one second
  unsigned long startTime = millis();
  while (millis() - startTime < 1000) {
    pulseCount += digitalRead(FLOW_SENSOR_PIN) == HIGH;
    delayMicroseconds(1000); // Wait for 1ms to debounce
  }

  // Calculate flow rate in L/min
  flowRate = pulseCount * 2.25;
  return flowRate;
}

// Adjust motor speed based on the PID output
void adjustMotorSpeed(double speed) {
  // Convert PID output to a motor speed value between 0 and 255
  int motor_Speed = map(output, -255, 255, 0, 255);

  // Set the motor speed using PWM
  analogWrite(MOTOR_PIN, motorSpeed);
}
void pulseCounter() {
  pulseCount++;
}

