import sys
from urllib.request import urlopen

# 'http://sixty-north.com/c/t.txt'
def fetch_words(url):
	story_words = []
	with urlopen(url) as story:
		for line in story:
			line_words = line.decode('utf-8').split()
			for word in line_words:
				story_words.append(word)
	return story_words

def print_words(story_words):
	print(type(story_words))
	for word in story_words:
		print(word)

def main(url):
	story_words = fetch_words(url)
	print_words(story_words)

if __name__ == '__main__':
	main('http://sixty-north.com/c/t.txt')
	#main(sys.argv[1])
