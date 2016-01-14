#probability_keyboard
This app displays a keyboard "heatmap" which shows the likeliest characters to follow a given string entry. 

Running **procEntryMap**() from the *simplified_script* module allows you to enter a word, letter by letter, and see how the most likely next letter changes as more letters are added to the string. A keyboard heatmap pops up on-screen after each letter is added, showing how likely a letter is to follow a string entry.

**Dependencies**:
* Python Imaging Library (PIL): **Image**, **ImageDraw**, **ImageFont**
* Numpy

**An example**

As a demonstration, here's the output from the first few letters of "orange." 

* First, I enter "o"; the [full string](http://imgur.com/vehue0r) is "o".
* Next, I enter "r"; the [full string](http://imgur.com/jHkOmSi) is now "or".
* Finally, I'll enter "a"; the [full string](http://imgur.com/HgRZv72) is now "ora".
