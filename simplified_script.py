from __future__ import division

# returns dictionary of all letters and their respective likelihoods to come after segment
def nextmostLikely(segment):
    segment = segment.lower()
    if segment not in words:
        raise Exception("\"%s\" is a word not contained in this corpus" % segment)  
    segment_dict_main = defaultdict(lambda: 0, {})
    word_list = []
    for w in words:
        if segment in w[:len(segment)] and len(w) > len(segment):  # ensure there's another letter to come
            word_list.append(w)             # all words that begin with segment (e.g. begin with 'pro')
    for w in word_list:
        # augment values in dictionary for the next letter after len(segment)
        segment_dict_main[w[len(segment)]] += 1
    segment_dict_perc = defaultdict(lambda: 0, {})
    count = sum(segment_dict_main[a] for a in alphabet)    # total number of words beginning with segment, longer than len(segment)
    if count == 0:
        raise Exception("\"%s\" is the only word of its kind in this corpus: unable to return next-letter probabilities" % segment)
    else:
        for a in alphabet:
            segment_dict_perc[a] = segment_dict_main[a]/count*100
        return segment_dict_perc

def changeColors(segment):
    # wipe the picture slate clean
    pic = Image.new("RGB", (800,200), "white")
    # get font from 'http://www5.miele.nl/apps/vg/nl/miele/mielea02.nsf/0e87ea0c369c2704c12568ac005c1831/07583f73269e053ac1257274003344e0?OpenDocument'
    font_path = "/Users/user/Documents/Python/probabilistic_keys/arial.ttf"
    font_let = ImageFont.truetype(font_path,25)
    font_perc = ImageFont.truetype(font_path,15)
    draw = ImageDraw.Draw(pic)
    for k,v in keyboard.items():
        x_min, x_max = v[0][0], v[0][1] # width bounds
        y_min, y_max = v[1][0], v[1][1] # height bounds
        perc = nextmostLikely(segment)[k]   # how often a letter appears
        new_color = int(perc/255*2000)  # scale how frequently a letter appears
        for i in range(x_min,x_max):    # width pixels
            for j in range(y_min, y_max):   # height pixels
                pic.putpixel((i,j), (255-new_color, 255-new_color, 255))
        xmean = int(np.average([x_min,x_max])-5)
        ymean = int(np.average([y_min,y_max])-25)
        draw.text((xmean,ymean),k,(0,0,0),font=font_let)
        draw.text((xmean-10,ymean+30),'{0:.2f}%'.format(perc),(0,0,0),font = font_perc)
        draw.text((int(width*0.75),int(height*0.75)),"Entry: \'%s\'"%segment,(0,0,0),font = font_let)
        draw = ImageDraw.Draw(pic)
    pic.show()

# run procEntryMap(); enter a letter and see the initial keyboard heatmap
# close the image and enter another letter to see the next keyboard heatmap
def procEntryMap():
    run = 0
    while True:
        initial = raw_input("Enter a letter, or press 'enter' to exit: \n")
        initial = initial.lower()
        if run == 0:
            res = '' + initial
        else:
            res += initial
        run += 1
        changeColors(res)   # show keyboard heatmap
        if not initial:
            break 
    
if __name__ == "__main__":

    import sys, os
    import string
    from string import ascii_lowercase
    from collections import defaultdict
    from PIL import Image, ImageDraw, ImageFont
    import numpy as np
    
    # add to PYTHONPATH a folder containing all necessary third-party modules
    sys.path.append("/Users/user/Documents/Python/added_modules")
    
    os.chdir("/Users/user/Documents/Python/probabilistic_keys")
    
    alphabet = list(string.ascii_lowercase)
    words = []
    
    # read-in Norvig Word Library. Obtained from 'http://norvig.com/ngrams/count_1w.txt'
    with open("Norvig Word Library.txt") as norvig_word_library:
        for line in norvig_word_library:
            (key,value) = line.split()
            words.append(key)

    # create a new image to get dimensions for keyboard dictionary creation
    pic = Image.new("RGB",(800,200),"white")
    width, height = pic.size[0], pic.size[1]
    x_incr, y_incr = int(width/10), int(height/3)
    
    # coordinates of each letter on a grid; {'letter':[(x_min,x_max),(y_min,y_max)]}
    keyboard = {
              # first row
              'q':[(0,x_incr),(0,y_incr)],'w':[(x_incr,2*x_incr),(0,y_incr)],
              'e':[(2*x_incr,3*x_incr),(0,y_incr)],'r':[(3*x_incr,4*x_incr),(0,y_incr)],
              't':[(4*x_incr,5*x_incr),(0,y_incr)],'y':[(5*x_incr,6*x_incr),(0,y_incr)],
              'u':[(6*x_incr,7*x_incr),(0,y_incr)],'i':[(7*x_incr,8*x_incr),(0,y_incr)],         
              'o':[(8*x_incr,9*x_incr),(0,y_incr)],'p':[(9*x_incr,10*x_incr),(0,y_incr)],
              
              # next row
              'a':[(0,x_incr),(y_incr,2*y_incr)],'s':[(x_incr,2*x_incr),(y_incr,2*y_incr)],
              'd':[(2*x_incr,3*x_incr),(y_incr,2*y_incr)],'f':[(3*x_incr,4*x_incr),(y_incr,2*y_incr)],
              'g':[(4*x_incr,5*x_incr),(y_incr,2*y_incr)],'h':[(5*x_incr,6*x_incr),(y_incr,2*y_incr)],
              'j':[(6*x_incr,7*x_incr),(y_incr,2*y_incr)],'k':[(7*x_incr,8*x_incr),(y_incr,2*y_incr)],
              'l':[(8*x_incr,9*x_incr),(y_incr,2*y_incr)],
    
              # final row
              'z':[(0,x_incr),(2*y_incr,3*y_incr)],'x':[(x_incr,2*x_incr),(2*y_incr,3*y_incr)],
              'c':[(2*x_incr,3*x_incr),(2*y_incr,3*y_incr)],'v':[(3*x_incr,4*x_incr),(2*y_incr,3*y_incr)],
              'b':[(4*x_incr,5*x_incr),(2*y_incr,3*y_incr)],'n':[(5*x_incr,6*x_incr),(2*y_incr,3*y_incr)],
              'm':[(6*x_incr,7*x_incr),(2*y_incr,3*y_incr)]
              }
    # run it
    procEntryMap()
