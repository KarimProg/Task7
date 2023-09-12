/*
 * File: Task7.2 .ino
 * Author: Group 6
 * Description: This code uses a PID controller to adjust the speed 
 *               of a motor based on the flow rate measured by a flow meter.
 * Date: [12/9/2023]
 */

/* Macros */
#include <PID_v1.h>

///< Initialize flow meter and motor pins
#define FLOW_SENSOR_PIN 2
#define MOTOR_PIN 3

volatile int pulseCount = 0;
float flowRate = 0;
int motorSpeed = 0;

// Define PID tuning parameters
double Kp = 1;  ///< Kp: Proportional gain
double Ki = 0.1;  ///< Ki: Integral gain
double Kd = 0.01;  ///< Kd: Derivative gain

// Define setpoint and input variables
double setpoint = 90;
double input = 0;

// Define output variable
double output = 0;

// Create PID controller object using PID_v1 library
PID myPID(&input, &output, &setpoint, Kp, Ki, Kd, DIRECT);

void setup() {
  // Initialize flow meter and motor
  pinMode(FLOW_SENSOR_PIN, INPUT_PULLUP); ///< Initialize flow sensor pin as input
  pinMode(MOTOR_PIN, OUTPUT); ///< Initialize motor pin as output
  digitalWrite(MOTOR_PIN, LOW);
  attachInterrupt(digitalPinToInterrupt(FLOW_SENSOR_PIN), pulseCounter, RISING);
  Serial.begin(9600);  ///< Initialize serial communication
}

void loop() {
  // Calculate flow rate and update motor speed accordingly
  flowRate = pulseCount * 2.25; ///<Convert pulses per second to L/min
  motorSpeed = map(flowRate, 0, 10, 0, 255);   ///< Convert flow rate to motor speed value
  analogWrite(MOTOR_PIN, motorSpeed);  ///< Send motorSpeed to MOTOR_PIN

  // Print flow rate and motor speed to serial monitor
  Serial.print("Flow rate: ");
  Serial.print(flowRate);
  Serial.print(" Motor speed: ");
  Serial.println(motorSpeed);

  pulseCount = 0; ///< Reset pulse count for next measurement
  delay(1000);

  input = flowRate; ///< Save flow meter readinf=g in the variable input
  myPID.Compute();  ///< Compute PID output
  adjustMotorSpeed(output);  ///< Adjust motor speed based on PID output
  delay(100);  ///< Wait for some time before repeating the loop
}


/**
 * @brief Adjusts the motor speed based on the PID output.
 *
 * This function takes the PID output and converts it to a motor speed value
 * between 0 and 255 using the map() function. It then sets the motor speed
 * using PWM.
 *
 * @param pid_Output The PID output value.
 */

void adjustMotorSpeed(double pid_Output) {
  int motor_Speed = map(pid_Output, -255, 255, 0, 255); ///< Convert PID output to a motor speed value between 0 and 255
  analogWrite(MOTOR_PIN, motor_Speed); ///< Set the motor speed using PWM
}

/**
 * @brief Interrupt service routine for counting pulses from flow meter.
 * This function is called whenever a pulse is detected on the flow meter pin. It increments the pulse count variable.
 * @param None
 * @return None
 */
void pulseCounter() {
  pulseCount++;
}

