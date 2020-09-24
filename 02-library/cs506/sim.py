
def euclidean_dist(x, y):
    #raise NotImplementedError()
    if (len(x) != len(y)):
        return "wrong dimensions"
    vectorSize = len(x)
    sum = 0
    for ind in range(vectorSize):
        sum += (x[ind] - y[ind])**2
    return sum**(0.5)
    
def manhattan_dist(x, y):
    #raise NotImplementedError()
    if (len(x) != len(y)):
        return "wrong dimensions"
    vectorSize = len(x)
    sum = 0
    for ind in range(vectorSize):
        sum += abs(x[ind] - y[ind])
    return sum
def jaccard_dist(x, y):
    #raise NotImplementedError()
    if (x == y):
        return 0
    a = set(x)
    b = set(y)
    
    #1 - jaccard index
    intersection_card = len(a.intersection(b))
    union_card = len(a.union(b))
    return 1 - intersection_card/union_card
    
def cosine_sim(x, y):
    #raise NotImplementedError()
    if (len(x) != len(y)):
        return "wrong dimensions"
        
    normedY = norm(y)
    normedX = norm(x)
    if (normedY == 0 or normedX == 0):
        return 1
    return dot(x, y)/(normedX*normedY)
    
# Feel free to add more

def dot(v1, v2):
    #took for stackoverflow
    return sum(x*y for x,y in zip(v1,v2))
    
def norm(field):
    sum = 0
    for i in field:
        sum += i**2
    return sum**(1/2)
    