WORDS = {
	line.split('\t')[0].strip().lower() 
	for line in open('../../assets/words.txt', 'r')
}