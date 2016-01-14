#probability_keyboard

This app displays a keyboard "heatmap" which shows the likeliest characters to follow a given string entry. 

Running **procEntryMap**() from the *simplified_script* module allows you to enter a word, letter by letter, and see how the most likely next letter changes as more letters are added to the string. A keyboard heatmap with these probabilities pops up onscreen after each letter is added.

**Dependencies**:
* Python Imaging Library (PIL): **Image**, **ImageDraw**, **ImageFont**
* Numpy

**Difference between *simplified_script* and *all_functions* modules?**

The *simplified_script* module provides all necessary components to display the output below, which is really what this app is about.

The *all_functions* module contains a variety of functions, allowing the user to explore relationships between letters at a more granular level. This script is an extension of the *simplified_script*, and allows the user to see where some of the structures in *simplified_script* came from.

**An example**

As a demonstration, here's the output from the first few letters of "orange." At each step of the process, the program calculates each letter's probability of occurring after the full string. So, a user might wonder how likely it is that an "n" follows "ora". This progression is observed below:

* First, enter "o"; the full string is now "o". !["o"](https://cloud.githubusercontent.com/assets/15989526/12326596/6876ffce-ba97-11e5-8699-84b2093c29df.png)

* Next, enter "r"; the full string is now "or". !["or"](https://cloud.githubusercontent.com/assets/15989526/12326598/6ce7f81a-ba97-11e5-9cea-f620f1814f71.png)

* Finally - to end this demonstration - enter "a"; the full string is now "ora". !["ora"](https://cloud.githubusercontent.com/assets/15989526/12326601/6f5a9300-ba97-11e5-9355-047d52c72f61.png)
