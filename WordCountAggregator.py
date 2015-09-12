__author__ = 'saipc'


def WordCountAggregator():
    with open('words', 'r') as file1:
        dictionary = {}
        for line in file1:
            word, count = line.split(" ", 1)
            if (word not in dictionary):
                dictionary[word] = count
            else:
                dictionary[word] = int(dictionary[word]) + int(count)
        print dictionary

WordCountAggregator()