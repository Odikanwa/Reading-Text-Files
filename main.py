# A program that reads text from a file, and count the occurence of words in that text
# - story

# Open file
story = open('story.txt')

# Read file
# - Arg is passed from function call. Value of story is already initialised
def read_file_content(story):
    return story.read()

# Count occurence of each word in the story
def count_words():
    text = read_file_content(story)

    # Split story into words
    words = text.split(' ')

    # Initialise a dictionary
    words_dict = dict()

    # If word doesn't exist, add to dict and set value as 1. If it does already, increment value by 1
    for word in words:
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1

    return print(words_dict)

count_words()

# Close file
story.close()
