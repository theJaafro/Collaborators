import numpy as np
import copy

# Functions
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

def NewNode(stateChange, newNode, nodeStates, nodeIndexs, parentNodes, count,\
 index, parent):
    """Inserts new node,
        if blank tile moves and node has not been visited"""
    if stateChange == 1:
        repeat = 0
        if newNode in nodeStates == True:
            repeat = 1

        if repeat == 0:
            count += 1
            index += 1
            nodeStates.append(newNode)
            nodeIndexs.append(index)
            parentNodes.append(parent)
    return nodeStates, nodeIndexs, parentNodes, count, index;

def generatePath(nodeStates, nodeIndexs, nodeParents):
    """Backtracks from final node to initial node"""
    states = nodeStates[::-1]
    indexs = nodeIndexs[::-1]
    parents = nodeParents[::-1]
    finalNode = states[0]
    print('FINAL NODE')
    print(finalNode)
    initialNode = states[-1]
    print('INITIAL NODE')
    print(initialNode)
    print('PATH')
    # i = parents[0]
    # j = indexs[0]
    # for i < j:
    #     if

# ===START===

# ---Get the initial node from the user---
initialNode = [[1, 2, 3],[4, 5, 6],[7, 0, 8]]
goalNode = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# ---Save node information using a data structure---
# The data structure chosen are lists
Node_State_i = []
Node_Index_i = [1]
Parent_Node_Index_i = [1]
counter = 0
indexCounter = 1
parentCounter = 1

Node_State_i.append(initialNode[:])

print('BEGIN')
print(Node_State_i)
print(Node_Index_i)
print(Parent_Node_Index_i)
cont = 'y'

# ---Apply actions to blank tile to generate new nodes---
# Check if the new node meets the goal node
while cont == 'y':
    # Move left
    print('MOVE LEFT')
    parent = parentCounter - 1
    [NewNodeState, stateChange] = ActionMoveLeft(Node_State_i[parent])

    # ---Check if node already exists in the data structure and add to data structure---
    [Node_State_i, Node_Index_i, Parent_Node_Index_i, counter, indexCounter] = \
    NewNode(stateChange, NewNodeState, Node_State_i, Node_Index_i, \
    Parent_Node_Index_i, counter, indexCounter, parentCounter)

    print(Node_State_i)
    print(Node_Index_i)
    print(Parent_Node_Index_i)

    if Node_State_i[counter] == goalNode:
        print('SUCCESS!')
        break

    # Move right
    print('MOVE RIGHT')
    [NewNodeState, stateChange] = ActionMoveRight(Node_State_i[parent])

    [Node_State_i, Node_Index_i, Parent_Node_Index_i, counter, indexCounter] = \
    NewNode(stateChange, NewNodeState, Node_State_i, Node_Index_i, \
    Parent_Node_Index_i, counter, indexCounter, parentCounter)

    print(Node_State_i)
    print(Node_Index_i)
    print(Parent_Node_Index_i)

    if Node_State_i[counter] == goalNode:
        print('SUCCESS!')
        break

    # Move up
    print('MOVE UP')
    [NewNodeState, stateChange] = ActionMoveUp(Node_State_i[parent])

    [Node_State_i, Node_Index_i, Parent_Node_Index_i, counter, indexCounter] = \
    NewNode(stateChange, NewNodeState, Node_State_i, Node_Index_i, \
    Parent_Node_Index_i, counter, indexCounter, parentCounter)

    print(Node_State_i)
    print(Node_Index_i)
    print(Parent_Node_Index_i)

    if Node_State_i[counter] == goalNode:
        print('SUCCESS!')
        break

    # Move down
    print('MOVE DOWN')
    [NewNodeState, stateChange] = ActionMoveDown(Node_State_i[parent])

    [Node_State_i, Node_Index_i, Parent_Node_Index_i, counter, indexCounter] = \
    NewNode(stateChange, NewNodeState, Node_State_i, Node_Index_i, \
    Parent_Node_Index_i, counter, indexCounter, parentCounter)

    print(Node_State_i)
    print(Node_Index_i)
    print(Parent_Node_Index_i)

    if Node_State_i[counter] == goalNode:
        print('SUCCESS!')
        break

    parentCounter =+ 1
    cont = input('Continue?')


# ---Back track to find the path---
generatePath(Node_State_i, Node_Index_i, Parent_Node_Index_i)

# ---Print path---

# ===END===


# def generate_path():
#     """Generates path by backtracking from
#         final node to initial node"""

# Prewritten from plot_path.py
# def print_matrix(state):
#     counter = 0
#     for row in range(0, len(state), 3):
#         if counter == 0 :
#             print("-------------")
#         for element in range(counter, len(state), 3):
#             if element <= counter:
#                 print("|", end=" ")
#             print(int(state[element]), "|", end=" ")
#         counter = counter +1
#         print("\n-------------")
# # Prewritten from plot_path.py
# fname = 'nodePath.txt'
# data = np.loadtxt(fname)
# if len(data[1]) is not 9:
#     print("Format of the text file is incorrect, retry ")
# else:
#     for i in range(0, len(data)):
#         if i == 0:
#             print("Start Node")
#         elif i == len(data)-1:
#             print("Achieved Goal Node")
#         else:
#             print("Step ",i)
#         print_matrix(data[i])
#         print()
#         print()
