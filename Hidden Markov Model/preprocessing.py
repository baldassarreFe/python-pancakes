import re

# keep everything that's a char, digit or whitespace
# discard punctuation and underscores
# return the text as a list
def sentence(text):
    result = re.sub(r"[^\w\s]|_","", text.lower()).split()
    return result

# returns a list of preprocessed sentences
def paragraph(text):
    sentences = [sentence(sent) for sent in re.split(r"[.!?]",text)]
    sentences = [sent for sent in sentences if len(sent) > 0]
    return sentences

# given preprocessed text returns an ordered list of unique words
def dictionary(preprocessedText):
    wordSet = set()
    for sentence in list(preprocessedText):
        wordSet.update(sentence)
    result = list(wordSet)
    result.sort()
    return result

if __name__ == '__main__':
    sent = "Just try'n with some text-based content!"
    print(sentence(sent))

    par = "But now it's time to try harder stuff: like #hashtags! Or maybe another PHRASE?"
    print(paragraph(par))

    print(dictionary(paragraph(par)))
