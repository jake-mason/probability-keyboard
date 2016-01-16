#probability_keyboard

An application of a [m-Order Markov Chain Letter Prediction](http://www.stat.purdue.edu/~mdw/CSOI/MarkovLab.html), this app displays a keyboard "heatmap" which shows the likeliest characters to follow a dynamic string entry. 

Running **procEntryMap**() from the *simplified_script* module allows you to enter a word, letter by letter, and see how the most likely next letter changes as more letters are added to the string. A keyboard heatmap with these probabilities pops up onscreen after each letter is added.

**Dependencies**:
* Python Imaging Library (PIL): **Image**, **ImageDraw**, **ImageFont**
* Numpy

**Difference between *simplified_script* and *all_functions* modules?**

The *simplified_script* module provides all necessary components to display the output below, which is really what this app is about.

The *all_functions* module contains a variety of functions, allowing the user to explore relationships between letters at a more granular level. This script is an extension of the *simplified_script*, and allows the user to see where some of the structures in *simplified_script* came from.

**An example**

As a demonstration, here's the output from the first few letters of "orange." At each step of the process, the program calculates each letter's probability of occurring after the full string. So, a user might wonder how likely it is that an "n" follows "ora". This progression is observed below:

* First, enter "o"; the full string is now "o". !["o"](http://i.imgur.com/jjQzYOK.png)

* Next, enter "r"; the full string is now "or". !["or"](http://i.imgur.com/ZXxkIzN.png)

* Finally - to end this demonstration - enter "a"; the full string is now "ora". !["ora"](http://i.imgur.com/NQGhvAj.png)
