from utils import updateProgress, binarySearch
import numpy as np
import gutenberg
import preprocessing

class MarkovModel():
    def __init__(self, dic):
        self.N = len(dic)
        self.dic = dic
        self.transitionFrequency = np.zeros((self.N, self.N), dtype=int)
        self.transitionProbability = np.random.rand(self.N,self.N)
        for row in range(self.N):
            self.transitionProbability[row] = self.transitionProbability[row] / self.transitionProbability[row].sum()

    def update(self, sequences):
        totalWords = sum([len(seq) for seq in list(sequences)])
        print("Updating model with:\n  sequences\t{0}\n  elements\t{1}".format(len(sequences), totalWords))
        processedWords = 0
        for sequence in list(sequences):
            # counting the occurrences of a transiton
            sequence = [binarySearch(self.dic, s) for s in sequence]
            for curr, succ in zip(sequence[:-1], sequence[1:]):
                self.transitionFrequency[curr, succ] += 1
                processedWords += 1
            processedWords+=1
            updateProgress(processedWords/totalWords)

        # recomputing the probabilities
        for row in range(self.N):
            if self.transitionFrequency[row].sum() != 0:
                self.transitionProbability[row] = self.transitionFrequency[row]
            else:
                self.transitionProbability[row] = np.random.rand()
            self.transitionProbability[row] /= self.transitionProbability[row].sum()

    def generate(self, initial=None, T=10):
        if initial is None:
            initial = self.dic[np.random.choice(self.N)]

        sequence = [binarySearch(self.dic, initial)]
        for t in range(T):
            transitionProb = self.transitionProbability[sequence[-1]]
            succ = np.random.choice(self.N, p=transitionProb)
            sequence.append(succ)
        return [self.dic[s] for s in sequence]

def exampleWithBook():
    sentences = preprocessing.paragraph(gutenberg.getBook(35534))
    dic = preprocessing.dictionary(sentences)
    mm = MarkovModel(dic)
    mm.update(sentences)
    for t in range(10):
        print(t,"\t"," ".join(mm.generate(T=15)))

def exampleWithCharacters():
    mm = MarkovModel("ABC")
    trainSequences1=["ABC"*40, "AABB"*30]
    mm.update(trainSequences1)
    for t in range(10):
        print(t,"\t","".join(mm.generate(T=15)))
    trainSequences2=["AAA"*40, "CCBB"*30]
    mm.update(trainSequences2)
    for t in range(10):
        print(t,"\t","".join(mm.generate(T=15)))

if __name__ == '__main__':
    exampleWithCharacters()
    exampleWithBook()
