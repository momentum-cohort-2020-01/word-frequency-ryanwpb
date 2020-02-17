STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

with open('seneca_falls.txt', 'r') as f:
    data = f.read()
    print(data)

    # define punctuation
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

# remove punctuation from the string
no_punct = ""
for char in data:
    if char not in punctuations:
        no_punct = no_punct + char

# display the unpunctuated string
new_text = no_punct.lower().split(" ")
print(new_text)
words_removed = []
for word in new_text:
    if word not in STOP_WORDS:
        words_removed += word
print(words_removed)


def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    pass


if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
