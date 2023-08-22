# Automated-Desktop
I wrote this basic python script with the intent of refreshing myself in Python, and learning how to autonomously navigate various software programs with minimal LOC.

## The overhead view

When executed, this script will record your mouse movements and clicks. Once you click the middle scroll button on the mouse, it will stop recording, and save your mouse's recorded movements in another Python script that you can run any time in order to re-play your mouse's movements.

While rudimentary, this program is already capable of automatically enrolling me in my Engineering courses the moment enrollment opens.

## How it works

This script utilizes the mouse library in Python to record the physical coordinates of the cursor every time a left or right click is made. It stores these movements and their associated click in a list, automatically filtering occurances where the same movement is repeated (as it records at such a speed that one mouse click may be recorded over ten times from the time it is pressed down to released).

Then, the program iterates through this list, creating a new Python file on your desktop and writing your mouse's behavior in Python within this new file.

## Improvements

There are a host of basic improvements that could be made:

- Using the pyautogui library to enable additional features, such as reading text on the computer screen, and recording and operating letters and hotkeys which would open the door to greater versatility (i.e. the location of a program behavior on the screen is variable (like closing a tab on Google), but operating the same feature via a hotkey works indepenendent of program placement on the screen (ctl + w in this example))
- Creating a GUI for the user when starting and ending the recording program, and for labelling the Python templates they create after recoring specific behavior
- Recording the relative time associated with every key / button clicked, so that the computer can imitate the time between tasks. This is especially useful for opening programs or windows that require a few seconds to load
