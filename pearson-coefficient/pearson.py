import numpy as np


def calcSimByPearson(x1, x2):
    x1Mean = np.nanmean(x1)
    x2Mean = np.nanmean(x2)

    conv = np.nansum((x1 - x1Mean) * (x2 - x2Mean))
    corr1 = np.sqrt(np.nansum((x1 - x1Mean) ** 2))
    corr2 = np.sqrt(np.nansum((x2 - x2Mean) ** 2))

    return conv / (corr1 * corr2)


def calcSim(X):
    n = X.shape[0]   # n is no. of rows i.e. no.of users
    sim = np.zeros((n, n), dtype='float')

    for i in range(n):
        for j in range(n):
            sim[i][j] = calcSimByPearson(X[i], X[j])

    return sim


def recommender(ratings):
    sim = calcSim(ratings)
    print("User similarity Matrix U")
    print("U[i][j] = similarity between users i and j")
    print()
    print(sim)
    print()

    # Applying user based nearest neighbour recommendation to predict rating
    ratingsAvg = np.nanmean(ratings, axis=1)

    ratingsPredicted = np.zeros(ratings.shape)

    for i in range(ratings.shape[0]):
        for j in range(ratings.shape[1]):
            if np.isnan(ratings[i][j]):

                num, den = 0, 0
                for iOthers in range(ratings.shape[0]):
                    if i != iOthers and not np.isnan(ratings[iOthers][j]) and sim[i][iOthers] > 0:
                        num += (ratings[iOthers][j] - ratingsAvg[iOthers]) * sim[i][iOthers]
                        den += sim[i][iOthers]

                ratingsPredicted[i][j] = ratingsAvg[i] + num / den
            else:
                ratingsPredicted[i][j] = ratings[i][j]

    
    print("After rating prediction the user-product-ratings table looks like:")
    print()
    print(ratingsPredicted)


# rows represent users, columns represent products
recommender(np.array(
    [
        [5, 3, 4, 4, np.nan],
        [3, 1, 2, 3, 3],
        [4, 3, 4, 3, 5],
        [3, 3, 1, 5, 4],
        [1, 5, 5, 2, 1],
    ]
))
