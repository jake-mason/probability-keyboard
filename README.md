#probability_keyboard
This app displays a keyboard "heatmap" which shows the likeliest characters to follow a given string entry. 

Running **procEntryMap**() from the *simplified_script* module allows you to enter a word, letter by letter, and see how the most likely next letter changes as more letters are added to the string. A keyboard heatmap pops up on-screen after each letter is added, showing how likely a letter is to follow a string entry.

**Dependencies**:
* Python Imaging Library (PIL): **Image**, **ImageDraw**, **ImageFont**
* Numpy

**An example**

As a demonstration, here's the output from the first few letters of "orange." 
* First, I enter "o"; here's the !['o' output](http://imgur.com/vehue0r). 
* Next, I enter 'r'; here's the !['or' output](http://imgur.com/jHkOmSi). 
* Finally, I'll enter 'a'; here's the !['ora' output](http://imgur.com/HgRZv72).
