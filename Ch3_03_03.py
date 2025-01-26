import numpy as np

data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]

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

    N = len(data)
    dist = np.empty((N, N), dtype=float)

    for i in range(N):
        for j in range(i + 1, N):
            dist[i, j] = taxicab(data[i], data[j])
            dist[j, i] = dist[i, j]

    '''
    # another way
    for i in range(N):
        for j in range(N):            
            if i == j:
                dist[i, j] = np.inf
            else:
                dist[i, j] = taxicab(data[i], data[j])
    '''

    print(np.unravel_index(np.argmin(dist), dist.shape))

find_nearest_pair(data)
