def A(w : [], v : [], i : int, j : int):

    """
    :param w: weights
    :param v: values
    :param i: current row
    :param j: column
    :return: maximum value with minimal weight
    """

    if i == 0 or j == 0:
        return 0

    if w[i] > j:
        return A( w, v, i - 1, j)

    if w[i] <= j:
        return max(A(w, v, i - 1, j), v[i - 1] + A(w, v, i - 1, j - w[i - 1]))
