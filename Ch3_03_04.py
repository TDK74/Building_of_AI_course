import numpy as np
import math


text = '''Humpty Dumpty sat on a wall
Humpty Dumpty had a great fall
all the king's horses and all the king's men
couldn't put Humpty together again'''

# I purposely made it with functions for all calculations
def split_text(text):
    """
    Split the text into lines and then into lists of words.

    Args:
        text (str): The text to be split.

    Returns:
        list: A list of lists containing words.
    """
    return [line.lower().split() for line in text.splitlines()]

def create_vocab(text):
    """
    Create the vocabulary: the list of words that appear at least once.

    Args:
        text (str): The text from which to create the vocabulary.

    Returns:
        list: A list of unique words.
    """
    return list(set(text.lower().split()))

def calculate_tf(word, docs):
    """
    Calculate the term frequency (TF) of a word in each document.

    Args:
        word (str): The word for which to calculate TF.
        docs (list): A list of documents.

    Returns:
        list: A list of TF values for the word in each document.
    """
    return [doc.count(word) / len(doc) for doc in docs]

def calculate_df(word, docs):
    """
    Calculate the document frequency (DF) of a word in the documents.

    Args:
        word (str): The word for which to calculate DF.
        docs (list): A list of documents.

    Returns:
        float: The DF value for the word.
    """
    return sum([word in doc for doc in docs]) / len(docs)

def calculate_tf_idf(tf, df):
    """
    Calculate the TF-IDF value for a word.

    Args:
        tf (float): The TF value of the word.
        df (float): The DF value of the word.

    Returns:
        float: The TF-IDF value.
    """
    return tf * math.log(1 / df, 10)

def taxicab(row1, row2):
    """
    Calculate the Manhattan (Taxicab) distance between two rows.

    Args:
        row1 (list): The first row of integer values.
        row2 (list): The second row of integer values.

    Returns:
        float: The Manhattan distance between the two rows.
    """
    return np.sum(np.abs(np.array(row1) - np.array(row2)))

def find_nearest_pair(data):
    """
    Find the pair of rows in the dataset with the smallest Manhattan distance.

    Args:
        data (list of lists): A list of rows, where each row is a list of integer values.

    Returns:
        tuple: A tuple containing the indices of the two rows with the smallest distance.
    """
    M = len(data)
    dist = np.empty((M, M), dtype=float)

    for i in range(M):
        for j in range(i + 1, M):
            dist[i, j] = taxicab(data[i], data[j])
            dist[j, i] = dist[i, j]

    np.fill_diagonal(dist, np.inf)

    return np.unravel_index(np.argmin(dist), dist.shape)

def main(text):
    """
    Main function to process the text and find the most similar pair of lines.

    Args:
        text (str): The input text.
    """

    # split the text first into lines and then into lists of words
    docs = split_text(text)

    # create the vocabulary - the list of words that appear at least once
    vocabulary = create_vocab(text)

    df = {}
    tf = {}

    for word in vocabulary:
        # tf - number of occurrences of word in document divided by document length
        tf[word] = calculate_tf(word, docs)

        # df - number of documents containing word
        df[word] = calculate_df(word, docs)

    all_tf_idf = []

    # Calculate the TF-IDF values for each document
    for doc_index, _ in enumerate(docs):
        tf_idf = []

        for word in vocabulary:
            tf_word = tf[word][doc_index]
            df_word = df[word]

            if df_word == 1:   # Check if the word appears in all documents
                tf_idf.append(0.0)
            else:
                # calculate and append the tf-idf values
                tf_idf.append(calculate_tf_idf(tf_word, df_word))

        all_tf_idf.append(tf_idf)

    data = np.array(all_tf_idf)

    result = find_nearest_pair(data)
    print(result)

main(text)
