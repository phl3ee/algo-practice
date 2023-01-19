def kWeakestRows(mat, k):

    #build output list(row, summed score of row)
    rowScores = []
    for row in range(len(mat)):
        rowScores.append([row, sum(mat[row])])

    #order it by summed score, then row, weakest first
    sortedresults = sorted(rowScores, key= lambda x:(x[1],x[0]))

    #output row up to k
    finaloutput = []
    for result in sortedresults[:k]:
        finaloutput.append(result[0])

    return finaloutput