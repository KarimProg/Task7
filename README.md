## Classes:
### PIDController:
> Members:   
1.  (double) **kp_**  
2.  (double) **ki_**    
3.  (double) **kd_**  
4.  (double) **setpoint_** 
5.  (double) **integral_**
6.  (double) **prevError_**
7.  (double) ***output_**

> Methods:   
1. **PIDController:**   
&nbsp;&nbsp;&nbsp;- The constructor to set the initial value.    
&nbsp;&nbsp;&nbsp;- Returning nothing.
2. **setGains:**    
&nbsp;&nbsp;&nbsp;- Set PID gains.    
&nbsp;&nbsp;&nbsp;- Returning noting.
3. **update:**    
&nbsp;&nbsp;&nbsp;- Update the PID controller with the current measurement.     
&nbsp;&nbsp;&nbsp;- Returning the adjusted output.