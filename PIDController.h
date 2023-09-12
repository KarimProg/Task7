#ifndef PIDCONTROLLER_H
#define PIDCONTROLLER_H

/**
 * @class PIDController
 * @brief PID Controller class for controlling the suction mechanism of an APC machine.
 */
class PIDController {
public:
    /**
     * @brief Constructor for PIDController.
     * @param kp Proportional gain.
     * @param ki Integral gain.
     * @param kd Derivative gain.
     * @param setpoint The desired setpoint (target flow rate in CFM).
     */
    PIDController(double kp, double ki, double kd, double setpoint);

    /**
     * @brief Set PID gains.
     * @param kp Proportional gain.
     * @param ki Integral gain.
     * @param kd Derivative gain.
     */
    void setGains(double kp, double ki, double kd);

    /**
     * @brief Update the PID controller with the current measurement.
     * @param measurement The current flow rate measurement in CFM.
     * @return The control output.
     */
    double update(double measurement);

private:
    double kp_;/// Proportional gain
    double ki_;/// Integral gain
    double kd_;/// Derivative gain
    double setpoint_;/// Target setpoint in CFM
    double integral_;/// Integral accumulator
    double prevError_;/// Previous error
    double output_;/// Control output
};

#endif
