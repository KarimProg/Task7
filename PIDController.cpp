#include "PIDController.h"

PIDController::PIDController(double kp, double ki, double kd, double setpoint)
    : kp_(kp), ki_(ki), kd_(kd), setpoint_(setpoint), integral_(0), prevError_(0), output_(0) {}

void PIDController::setGains(double kp, double ki, double kd) {
    kp_ = kp;
    ki_ = ki;
    kd_ = kd;
}

double PIDController::update(double measurement) {
    /// Calculate error
    double error = setpoint_ - measurement;

    /// Calculate the integral term with anti-windup protection
    integral_ += error;
    if (integral_ > 100) { /// Add your own anti-windup threshold here
        integral_ = 100;
    } else if (integral_ < -100) {
        integral_ = -100;
    }

    /// Calculate the derivative term
    double derivative = error - prevError_;
    
    /// Calculate the control output
    output_ = (kp_ * error) + (ki_ * integral_) + (kd_ * derivative);

    /// Store the current error for the next iteration
    prevError_ = error;

    return output_;
}
