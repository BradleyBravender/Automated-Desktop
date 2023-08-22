# WiFi-RC-Car
I am repurposing an remote control (RC) car to deploy TensorFlow Lite so that it can follow another vehicle via computer vision. This project is that other vehicle.

This project is my transformation of the remote controlled chassis of the pursued car into a car remotely controlled over SSH by a Raspberry Pi 2. The initial python script was adpated from https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/ for the sake of time, but then modified to meet the needs of this project.

The RC car has two motors: one for steering, and one for driving. Thus, keyboard commands on the client computer must be able to control the forward/backward and left/right rotations for motor_1 and motor_2 respectively.

Currently, the keys used are as follows:

'l' for left.
's' for straight.
'r' for right.

'f' for forward.
'b' for backward.

'h' to halt (stop) both motors.
'e' to exit the script and clean up the GPIO pins

