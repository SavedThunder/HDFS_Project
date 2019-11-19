

import sys

if __name__ == "__main__":

    # Reducer

    # Dictionaries for each adj list
    directed_dict = {}
    undirected_dict = {}

    # Nodes to keep track of for tasks 4 & 5
    longest_adj_dir = 0
    longest_adj_undir = 0
    min_dir = 0
    min_undir = 0

    for line in sys.stdin:

        # Pre process
        line = line.rstrip()
        line = line.split(' ')

        # Set initial longest/minimum connect so no key errors when searching dictionaries
        if len(undirected_dict) == 0:
            longest_adj_dir = line[0]
            min_undir = line[1]
        if len(directed_dict) == 0:
            longest_adj_undir = line[0]
            min_dir = line[1]

        # Directed Graph
        if line[0] not in directed_dict:
            directed_dict[line[0]] = [line[1]]
        elif line[0] in directed_dict:
            directed_dict[line[0]].append(line[1])
        if line[1] not in directed_dict:
            directed_dict[line[1]] = []

        # Minimum connected node directed
        if len(directed_dict[min_dir]) > len(directed_dict[line[1]]):
            min_dir = line[1]
        if len(directed_dict[min_dir]) > len(directed_dict[line[0]]):
            min_dir = line[0]

        #Checking aginst most connected (dir)
        if len(directed_dict[line[0]]) > len(directed_dict[longest_adj_dir]):
            longest_adj_dir = line[0]

        # Undirected Graph
        if line[0] not in undirected_dict:
            undirected_dict[line[0]] = [line[1]]
        elif line[0] in undirected_dict:
            undirected_dict[line[0]].append(line[1])
        if line[1] not in undirected_dict:
            undirected_dict[line[1]] = [line[0]]
        elif line[1] in undirected_dict:
            undirected_dict[line[1]].append(line[0])

        # Checking against current minimum connected (und)
        if len(undirected_dict[min_undir]) > len(undirected_dict[line[1]]):
            min_undir = line[1]
        if len(undirected_dict[min_undir]) > len(undirected_dict[line[0]]):
            min_undir = line[0]

        # Checking against current maximum connected (und)        
        if len(undirected_dict[line[0]]) > len(undirected_dict[longest_adj_undir]):
            longest_adj_undir = line[0]
        if len(undirected_dict[line[1]]) > len(undirected_dict[longest_adj_undir]):
            longest_adj_undir = line[1]

    sys.stdout.write("Longest Adj List Directed: " + str(directed_dict[longest_adj_dir]) + " - " + str(len(directed_dict[longest_adj_dir])))
    sys.stdout.write("\n\n")
    sys.stdout.write("Longest Adj List Undirected: " + str(undirected_dict[longest_adj_undir]) + " - " + str(len(undirected_dict[longest_adj_undir])))
    sys.stdout.write("\n\n")
    sys.stdout.write("Most connected node (dir): " + longest_adj_dir + " connections - " + str(len(directed_dict[longest_adj_dir])))
    sys.stdout.write("\n\n")
    sys.stdout.write("Most connected node (undir): " + longest_adj_undir + " connections - " + str(len(undirected_dict[longest_adj_undir])))
    sys.stdout.write("\n\n")
    sys.stdout.write("Least connected node (dir): " + min_dir + " connections - " + str(len(directed_dict[min_dir])))
    sys.stdout.write("\n\n")
    sys.stdout.write("Least connected node (undir): " + min_undir + " connections - " + str(len(undirected_dict[min_undir])))
