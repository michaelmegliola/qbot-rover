# qbot-rover
Simple 'Mars rover' example using the Qbot hardware

This is intended to be used with the QBot hardware project, the full repo for that can be found at https://github.com/LoisLab/qbot/

Maybe you've just built your robot and you want to test the hardware, or you're not quite ready to dive into machine learning, or maybe you have other ideas for your Qbot.  This project is a simple way to make sure everything is working and get you more familiar with the Raspberry Pi, python, and talking to external parts like stepper motors.

Take a peek at the code.  You'll see that it imports our Stepper/Steppers libraries and creates a new Rover class.  The rover, as implemented, can move forward, left, or right.  It's capable of a lot more, but you'll have to expand it on your own.

Follow the PDF instructions to set up your Pi with the OS, python, GPIO libraries.  Optionally, you can plug in a Raspberry Pi Camera module and get live video back from your rover (wirelessly!) in real time if you also install the mjpeg streaming package.

If you use a camera, you may want to print out the included STL file to give you a place to stick the camera unit.  The part mounts to your Qbot using the same bolts that hold your Raspberry Pi to the robot frame, on the side closest to the camera header (opposite side from the memory card slot).  It's sized for the "spy camera" sized module; feel free to hack the part in TinkerCAD if you need a bigger mount surface, but using some double-sided tape will work fine.

Have fun, let us know how you're doing, and reach out if you need help!

Software - michael@loislab.org
Hardware - jeff@loislab.org
