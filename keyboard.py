def next_most_likely(segment):
    '''
    Finds the letters most likely to follow a given string
    
    Parameters:
        segment: str
    
    Returns:
        If no words follow a given segment, an Exception is raised. Otherwise:
            
        percs: dict, how often (percentage-wise) each letter in ascii_lowercase
                    occurs following `segment`
                    

    '''
    segment = segment.lower().strip()
    
    # if segment isn't an "ordered subset" of *any* word in WORDS
    # then an exception should be raised, as that segment doesn't exist in this corpus
    if not any(segment in word for word in WORDS):
        print("'%s' is not contained within any word in this corpus" % segment)
        sys.exit(1)
        
    # number of characters in the segment
    n_chars = len(segment)
    
    # use > instead of >= to ensure that there's another character to come
    # or could add functionality to signal "end-of-word" "key"
    contained = {w for w in WORDS if segment in w[:n_chars] and len(w) > n_chars}

    counts = {letter: sum(1 for word in contained if word[n_chars] == letter)
                for letter in ascii_lowercase}
    
    # total number of words beginning with segment and longer than len(segment)
    count = sum(counts.values())  
    
    if not count:
        print("\nNo letters come after '%s' in this corpus. Unable to"
              " return next-letter probabilities.\n" % segment)
        sys.exit(1)
    else:
        # dict comprehension faster than defaultdict object
        percs = {letter: counts[letter]/count*100 
                 for letter in ascii_lowercase}
        return percs
        
def change_colors(segment):
    '''
    Updates the colors on the on-screen keyboard for a given segment.
    
    Parameters:
        segment: str
    '''
    # wipe the slate clean
    pic = Image.new("RGB", (800, 200), "white")
    
    # get font from 'http://www5.miele.nl/apps/vg/nl/miele/mielea02.nsf/0e87ea0c369c2704c12568ac005c1831/07583f73269e053ac1257274003344e0?OpenDocument'
    font_path = "../Documents/Python/probabilistic_keys/arial.ttf"
    font_let = ImageFont.truetype(font_path, 25)
    font_perc = ImageFont.truetype(font_path, 15)
    
    draw = ImageDraw.Draw(pic)
    
    for k,v in keyboard.items():
        # width bounds
        x_min, x_max = v[0][0], v[0][1]

        # height bounds
        y_min, y_max = v[1][0], v[1][1]
        
        # how often letter `k` appears
        perc = next_most_likely(segment)[k]

        # scale color
        new_color = int(perc/255*2000)
        
        for i in range(x_min, x_max):    # width pixels
            for j in range(y_min, y_max):   # height pixels
                pic.putpixel((i,j), (255-new_color, 255-new_color, 255))
                
        xmean = int(np.mean([x_min, x_max])-5)
        ymean = int(np.mean([y_min, y_max])-25)
        
        draw.text((xmean, ymean),
                  k,
                  (0, 0, 0),
                  font=font_let)
        
        draw.text((xmean-10,  ymean+30),
                  '{0:.2f}%'.format(perc),
                  (0, 0, 0),
                  font = font_perc)
        
        draw = ImageDraw.Draw(pic)
        
    draw.text((int(width*0.75), int(height*0.75)),
          "Entry: '%s'" % segment,
          (0, 0, 0),
          font = font_let)
    draw = ImageDraw.Draw(pic)
    
    pic.show()

# run run(); enter a letter and see the initial keyboard heatmap
# close the image and enter another letter to see the next keyboard heatmap
def main():
    run = 0
    while True:
        entry = input("Enter a letter, or press the "
                        "Enter key to exit: \n").lower().strip()
        if not entry:
            break
        else:
            if run == 0:
                word = '' + entry
            else:
                word += entry
        run += 1
        change_colors(word)   # show keyboard heatmap

if __name__ == "__main__":

    import os, sys
    from string import ascii_lowercase
    from collections import defaultdict
    from PIL import Image, ImageDraw, ImageFont
    import numpy as np
    
    # read-in Norvig Word Library. Obtained from 'http://norvig.com/ngrams/count_1w.txt'
    WORDS = {line.split("\t")[0].strip().lower() 
                for line in open("Norvig Word Library.txt", "r")}
    
    # create a new image to get dimensions for keyboard dictionary creation
    pic = Image.new("RGB", (800,200), "white")
    width, height = pic.size[0], pic.size[1]
    x_incr, y_incr = int(width/10), int(height/3)
    
    # keyboard rows
    rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
 
    # coordinates of each letter on a grid
    # {`letter`: [(x_min, x_max), (y_min, y_max)]}
    keyboard = {letter: [(j*x_incr, (j+1)*x_incr), (i*y_incr, (i+1)*y_incr)] 
                         for i, row in enumerate(rows)
                         for j, letter in enumerate(row)}
   
    # run it
    main()
