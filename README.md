# Drone_Control
For general xbox joystick and button controller reading, I created the The xbox_controller_general.py script which uses pygame to read the console input. Make sure that the controller is bluetooth paired to the computer. I found the joysticks to be somewhat finnicky so you may want to mess with the thresholds for different movements to trigger and take off the FIR filter I added.

I used the record_and_move.py script to shoot a recording while flying and have facial recognition. From the facial recognition you can command the drone to do things, like follow the face when you move relative to the drone (albeit slowly) or do a trick after some time liek flip. You can also use the xbox controller to take pictures and speed up slow down, turn, rotate, land, takeoff, etc.



A video example of the controller in action can be found at https://youtu.be/YPtIvC1LSLE 

![drone_image](/Images/combined_drone.jpg)