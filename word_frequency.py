from collections import Counter
STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

with open('seneca_falls.txt', 'r') as f:
    data = f.read()

    # define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# remove punctuation from the string
no_punct = ""
for char in data:
    if char not in punctuations:
        no_punct = no_punct + char

# display the unpunctuated string
words = no_punct.lower().split(" ")

for word in list(words):  # iterating on a copy since removing will mess things up
    if word in STOP_WORDS:
        words.remove(word)

count_words = Counter(words)
print("HERE ", count_words)
# def print_word_freq(file):
#     """Read in `file` and print out the frequency of words in that file."""
#     pass


# if __name__ == "__main__":
#     import argparse
#     from pathlib import Path

#     parser = argparse.ArgumentParser(
#         description='Get the word frequency in a text file.')
#     parser.add_argument('file', help='file to read')
#     args = parser.parse_args()

#     file = Path(args.file)
#     if file.is_file():
#         print_word_freq(file)
#     else:
#         print(f"{file} does not exist!")
#         exit(1)
