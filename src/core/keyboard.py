from string import ascii_lowercase
from collections import defaultdict
import statistics

from assets import WORDS

def next_most_likely(segment):
	'''
	Finds the letters most likely to follow a given string.
	
	Parameters:
		segment: str
	
	Returns:
		If no words follow a given segment, the program exits. Otherwise:

		percs: dict, how often (percentage-wise) each letter in ascii_lowercase
					occurs following `segment`
	'''

	segment = segment.lower().strip()

	# if segment isn't an 'ordered subset' of *any* word in WORDS
	# then an exception should be raised, as that segment doesn't exist in this corpus
	if not any(segment in word for word in WORDS):
		return None

	# number of characters in the segment
	n_chars = len(segment)
	
	# use > instead of >= to ensure that there's another character to come
	# or could add functionality to signal "end-of-word" "key"
	contained = {w for w in WORDS if segment in w[:n_chars] and len(w) > n_chars}

	counts = {
		letter: sum(1 for word in contained if word[n_chars] == letter)
		for letter in ascii_lowercase
	}
	
	# total number of words beginning with segment and longer than len(segment)
	count = sum(counts.values())  
	
	if not count:
		print(
			"\nNo letters come after '%s' in this corpus. Unable to"
			" return next-letter probabilities.\n" % segment
		)
		sys.exit(1)
	else:
		# dict comprehension faster than defaultdict object
		percs = {
			letter: counts[letter] / count * 100
			for letter in ascii_lowercase
		}
		return percs