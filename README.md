## SDSS Computing Studies Python Assignment
### More Binding

Objectives:
* Adding sound effects to a TKinter GUI

We can also bind functions to widgets that do more than just receive input and display output.  Sound effects can also be added to the callback functions that are created and bound to events.  These can be easily incorporated using a module and playing mp3 sound files.

We will need to install the *playsound* module
```
pip install playsound
```

Once the module is installed, it can be used in python:
```
import playsound

playsound.playsound("file.mp3")
```
or
```
from playsound import playsound

playsound("file.mp3")
```


### 2 Tasks

##### Task 1
Create a sound board.
This is a collection of buttons that is each bound to a sound effect.  These are great ways to help teach little children the different sounds that animals make, especially if you can add an image of the animal to the button.
You can choose what sound effects to include in your sound board.  Early sound boards were just sampled music bound to electronic keyboards: https://www.youtube.com/watch?v=z0PJnc8BFTk

##### Task 2
Create a math based game to test a student.
Give them 10 questions to answer.  
You will be graded based on the difficulty of the assignment:
Easy : Computation questions
Medium: Solving one step equations
Hard: Factoring questions
Keep score for the player and play appropriate sound effects when buttons are pressed
