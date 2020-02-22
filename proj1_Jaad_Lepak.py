import numpy as np
import copy
import os

# ENPM 661
# JAAD LEPAK
# 2020 02 21
# PROJECT 1

# ===== SECTION 1: INPUT =====
# INPUT THE PUZZLE YOU WOULD LIKE TO SOLVE IN VARIABLE 'initialNode'
# 
# LIST MUST BE INSERTED IN COLUMN-BASED FORMAT
#
# EXAMPLE:
# -------------
# | 1 | 2 | 3 | 
# -------------
# | 4 | 5 | 6 | 
# -------------
# | 7 | 8 | 0 | 
# -------------
#
# The puzzle above in list form is:
# [[1, 4, 7], [2, 5, 8], [3, 6, 0]]
#
initialNode = [[1, 0, 7], [8, 4, 6], [2, 3, 5]]
#
# =============================


# ===== SECTION 2: FUNCTIONS =====
    
def BlankTileLocation(CurrentNode):
    """Finds location of blank tile
        Returns output as pair (i,j)
        where 0<i<4 and 0<j<4"""
    i = 1
    for list in CurrentNode:
        j = 1
        for number in list:
            if number == 0:
                blank_i = i
                blank_j = j
                break
            j += 1
        i += 1
    return [blank_i,blank_j];

def ActionMoveLeft(CurrentNode):
    """Move tile LEFT, if possible"""
    NewNode = copy.deepcopy(CurrentNode)
    [i,j] = BlankTileLocation(CurrentNode[:])
    stateChange = 0
    if j != 1:
        i -= 1
        j -= 1
        j_left = j - 1
        numTile = CurrentNode[i][j_left]
        NewNode[i][j] = numTile
        NewNode[i][j_left] = 0
        stateChange = 1
    return NewNode[:], stateChange;

def ActionMoveRight(CurrentNode):
    """Move tile RIGHT, if possible"""
    NewNode = copy.deepcopy(CurrentNode)
    [i,j] = BlankTileLocation(CurrentNode[:])
    stateChange = 0
    if j != 3:
        i -= 1
        j -= 1
        j_right = j + 1
        numTile = CurrentNode[i][j_right]
        NewNode[i][j] = numTile
        NewNode[i][j_right] = 0
        stateChange = 1
    return NewNode[:], stateChange;

def ActionMoveUp(CurrentNode):
     """Move tile UP, if possible"""
     NewNode = copy.deepcopy(CurrentNode)
     [i,j] = BlankTileLocation(CurrentNode[:])
     stateChange = 0
     if i != 1:
         i -= 1
         j -= 1
         i_up = i - 1
         numTile = CurrentNode[i_up][j]
         NewNode[i][j] = numTile
         NewNode[i_up][j] = 0
         stateChange = 1
     return NewNode[:], stateChange;

def ActionMoveDown(CurrentNode):
     """Move tile DOWN, if possible"""
     NewNode = copy.deepcopy(CurrentNode)
     [i,j] = BlankTileLocation(CurrentNode[:])
     stateChange = 0
     if i != 3:
         i -= 1
         j -= 1
         i_down = i + 1
         numTile = CurrentNode[i_down][j]
         NewNode[i][j] = numTile
         NewNode[i_down][j] = 0
         stateChange = 1
     return NewNode[:], stateChange;

def list2num(node):
    """Converts a 3x3 array into one integer"""
    n = 1e8
    new = 0
    for list in node:
        for number in list:
            new += number*n
            n /= 10
    return new;

def NewNode(stateChange, newNode, nodeStates, nodeIndexs, parentNodes, count,\
 index, parent):
    """Inserts new node,
        if blank tile moves and node has not been visited"""
    if stateChange == 1:
        repeat = 0
        newNodeCheck = list2num(newNode)
        for list in nodeStates:
            check = list2num(copy.deepcopy(list))
            if newNodeCheck == check:
                repeat = 1
        if repeat == 0:
            count += 1
            index += 1
            nodeStates.append(newNode)
            nodeIndexs.append(index)
            parentNodes.append(parent)
            printNode(newNode)
    return nodeStates, nodeIndexs, parentNodes, count, index;

def generatePath(nodeStates, nodeIndexs, nodeParents):
    """Backtracks from final node to initial node"""
    states = nodeStates[::-1]
    indexs = nodeIndexs[::-1]
    parents = nodeParents[::-1]
    finalNode = [states[0]]
    initialNode = states[-1]
    parent = parents[0]
    child = indexs[0]
    finalParent = [parent]
    finalChild = [child]
    while child > 1:
        count = indexs.index(child)
        finalNode.insert(0,states[count])
        finalParent.insert(0,parents[count])
        finalChild.insert(0,indexs[count])
        child = parents[count]
        if child == 1:
            finalNode.insert(0,initialNode)
            break
    path = finalNode[:]
    return path, finalChild, finalParent;

def printPath(path, finalChild, finalParent):
    """Exports nodes to nodePath.txt as '1 4 7 2 5 8 3 6 0' on each new line,
    Exports child and parent nodes to NodesInfo.txt"""
    pathFile = open('nodePath.txt','a')
    for list in path:
    	for list in list:
    		for number in list:
    			pathFile.write(str(number) + ' ')
    	pathFile.write('\n')
    pathFile.close()
    nodeFile = open('NodesInfo.txt','a')
    i = 0
    for number in finalChild:
    	nodeFile.write(str(finalChild[i]) + ' ' + str(finalParent[i]) + '\n')
    	i += 1
    nodeFile.close()

def printNode(node):
    """Exports explored node to Nodes.txt as '1 4 7 2 5 8 3 6 0' on each new line"""
    nodeFile = open('Nodes.txt','a')
    for list in node:
        for number in list:
            nodeFile.write(str(number) + ' ')
    nodeFile.write('\n')
    nodeFile.close()
        

# ===== SECTION 3: EXPLORE =====

# Get the initial node from the user
goalNode = [[1, 4, 7], [2, 5, 8], [3, 6, 0]]


# Save node information using a data structure
# The data structure chosen are lists
Node_State_i = []
Node_Index_i = [1]
Parent_Node_Index_i = [1]
counter = 0
indexCounter = 1
parentCounter = 1

Node_State_i.append(initialNode[:])

# Remove any previously existing files
if os.path.exists('Nodes.txt'):
    os.remove('Nodes.txt')
if os.path.exists('NodesInfo.txt'):
    os.remove('NodesInfo.txt')
if os.path.exists('nodePath.txt'):
    os.remove('nodePath.txt')

# Let the user know the program has started
print('NOW SOLVING FOR')
print(Node_State_i)
print('\nCalculating...\n')

# Apply actions to blank tile to generate new nodes
# Check if the new node meets the goal node
while initialNode != goalNode:

    # Move left
    parent = parentCounter - 1
    [NewNodeState, stateChange] = ActionMoveLeft(Node_State_i[parent])
    
    # Check if node already exists in the data structure and add to data structure
    [Node_State_i, Node_Index_i, Parent_Node_Index_i, counter, indexCounter] = \
    NewNode(stateChange, NewNodeState, Node_State_i, Node_Index_i, \
    Parent_Node_Index_i, counter, indexCounter, parentCounter)


    if Node_State_i[counter] == goalNode:
        print('SUCCESS!\n')
        break

    # Move right
    [NewNodeState, stateChange] = ActionMoveRight(Node_State_i[parent])

    [Node_State_i, Node_Index_i, Parent_Node_Index_i, counter, indexCounter] = \
    NewNode(stateChange, NewNodeState, Node_State_i, Node_Index_i, \
    Parent_Node_Index_i, counter, indexCounter, parentCounter)


    if Node_State_i[counter] == goalNode:
        print('SUCCESS!\n')
        break

    # Move up
    [NewNodeState, stateChange] = ActionMoveUp(Node_State_i[parent])

    [Node_State_i, Node_Index_i, Parent_Node_Index_i, counter, indexCounter] = \
    NewNode(stateChange, NewNodeState, Node_State_i, Node_Index_i, \
    Parent_Node_Index_i, counter, indexCounter, parentCounter)


    if Node_State_i[counter] == goalNode:
        print('SUCCESS!\n')
        break

    # Move down
    [NewNodeState, stateChange] = ActionMoveDown(Node_State_i[parent])

    [Node_State_i, Node_Index_i, Parent_Node_Index_i, counter, indexCounter] = \
    NewNode(stateChange, NewNodeState, Node_State_i, Node_Index_i, \
    Parent_Node_Index_i, counter, indexCounter, parentCounter)


    if Node_State_i[counter] == goalNode:
        print('SUCCESS!\n')
        break

    if parentCounter % 100 == 0:
        print('Still Calculating...\n')
        if parentCounter % 500 == 0:
                print('Puzzle may be unsolvable...\n')

    parentCounter += 1


# Back track to find the path
[finalNodes, finalChilds, finalParents] = generatePath(Node_State_i, Node_Index_i, Parent_Node_Index_i)

# ===== SECTION 4: PRINT =====
# Print path
printPath(finalNodes, finalChilds, finalParents)
			       
# Prewritten from plot_path.py
def print_matrix(state):
    counter = 0
    for row in range(0, len(state), 3):
        if counter == 0 :
            print("-------------")
        for element in range(counter, len(state), 3):
            if element <= counter:
                print("|", end=" ")
            print(int(state[element]), "|", end=" ")
        counter = counter +1
        print("\n-------------")
fname = 'nodePath.txt'
data = np.loadtxt(fname)
if len(data[1]) is not 9:
    print("Format of the text file is incorrect, retry ")
else:
    for i in range(0, len(data)):
        if i == 0:
            print("Start Node")
        elif i == len(data)-1:
            print("Achieved Goal Node")
        else:
            print("Step ",i)
        print_matrix(data[i])
        print()
        print()
# ===== END =====
