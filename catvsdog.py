import sys
from bipartite_match import bipartiteMatch



def build_structures(test_case):
    # All the dog lovers by their dog vote.
    dog_lovers_by_dog = {}
    # Dog lovers by their cat vote
    dog_lovers_by_cat = {}
    # All the cat lovers
    cat_lovers = []
    # Dictionary for building a bipartite graph
    graph = {}

    # get the test details and remove it from the list
    dogs, cats, total_votes = test_case.pop(0)


    # Build the base datastructures
    count = 0
    for vote in test_case:
        vote.append(count)
        if vote[0][0] == 'D':
            if vote[0] in dog_lovers_by_dog:
                dog_lovers_by_dog[vote[0]].append(vote)
            else:
                dog_lovers_by_dog[vote[0]] = vote

            if vote[1] in dog_lovers_by_cat:
                dog_lovers_by_cat[vote[1]].append(vote)
            else:
                dog_lovers_by_cat[vote[1]] = vote
        else:
            cat_lovers.append(vote)
        count += 1

    # Build the graph
    for cat_vote in cat_lovers:
        x = []
        try:
            x.append(' '.join(map(str, dog_lovers_by_dog.get(cat_vote[1]))))
        except:
            pass
        try:
            x.append(' '.join(map(str, dog_lovers_by_cat.get(cat_vote[0]))))
        except:
            pass
        graph[' '.join(map(str, cat_vote))] = set(x)

    # Process the graph vi David Eppstein's max-cardinality module
    matching = bipartiteMatch(graph)[0]
    print str(int(total_votes) - len(matching))




def main():
    tests = []

    # Get inputs
    count = 0
    for line in sys.stdin:
        line = line.rstrip('\n')
        tests.append(line.split(' '))
        count += 1

    # Built datastructure
    results = int(tests.pop(0)[0])
    test_cases = []
    while tests:
        y = []
        votes = int(tests[0][2])
        count = 0
        while count <= votes:
            y.append(tests.pop(0))
            count += 1
        test_cases.append(y)

    # Run through each test case
    for test_case in test_cases:
        build_structures(test_case)




if __name__ == "__main__":
    sys.exit(main())
