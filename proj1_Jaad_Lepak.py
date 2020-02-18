import numpy as np

# Parameters
Node_State_i = [[1, 2, 0],[4, 5, 6],[8, 3, 7]]
Node_Index_i = 0
Parent_Note_Index_i = 0

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

# TESTING
print('FINDING BLANK TILE LOCATION TEST')
print(Node_State_i)
[i,j] = BlankTileLocation(Node_State_i)
print(i,j)
# END TESTING

def ActionMoveLeft(CurrentNode):
    """Move tile LEFT, if possible"""
    NewNode = CurrentNode
    [i,j] = BlankTileLocation(CurrentNode)
    print('while moving left, here is the blank tile location before moving')
    print(i,j)
    stateChange = 0
    if j != 1:
        i -= 1
        j -= 1
        j_left = j - 1
        numTile = CurrentNode[i][j_left]
        NewNode[i][j] = numTile
        NewNode[i][j_left] = 0
        stateChange = 1
    return NewNode, stateChange;

# TESTING
print('MOVING TILE LEFT, IF POSSIBLE, TEST')
print(Node_State_i)
[Node_State_i, stateChange] = ActionMoveLeft(Node_State_i)
print(Node_State_i)
print(stateChange)
# END TESTING

def ActionMoveRight(CurrentNode):
    """Move tile RIGHT, if possible"""
    NewNode = CurrentNode
    [i,j] = BlankTileLocation(CurrentNode)
    print('while moving right, here is the blank tile location before moving')
    print(i,j)
    stateChange = 0
    if j != 3:
        i -= 1
        j -= 1
        j_right = j + 1
        numTile = CurrentNode[i][j_right]
        NewNode[i][j] = numTile
        NewNode[i][j_right] = 0
        stateChange = 1
    return NewNode, stateChange;

# TESTING
print('MOVING TILE RIGHT, IF POSSIBLE, TEST')
print(Node_State_i)
[Node_State_i, stateChange] = ActionMoveRight(Node_State_i)
print(Node_State_i)
print(stateChange)
# END TESTING

def ActionMoveUp(CurrentNode):
     """Move tile UP, if possible"""
     NewNode = CurrentNode
     [i,j] = BlankTileLocation(CurrentNode)
     print('while moving up, here is the blank tile location before moving')
     print(i,j)
     stateChange = 0
     if i != 1:
         i -= 1
         j -= 1
         i_up = i - 1
         numTile = CurrentNode[i_up][j]
         NewNode[i][j] = numTile
         NewNode[i_up][j] = 0
         stateChange = 1
     return NewNode, stateChange;

# TESTING
print('MOVING TILE UP, IF POSSIBLE, TEST')
print(Node_State_i)
[Node_State_i, stateChange] = ActionMoveUp(Node_State_i)
print(Node_State_i)
print(stateChange)
# END TESTING

def ActionMoveDown(CurrentNode):
     """Move tile DOWN, if possible"""
     NewNode = CurrentNode
     [i,j] = BlankTileLocation(CurrentNode)
     print('while moving down, here is the blank tile location before moving')
     print(i,j)
     stateChange = 0
     if i != 3:
         i -= 1
         j -= 1
         i_down = i + 1
         numTile = CurrentNode[i_down][j]
         NewNode[i][j] = numTile
         NewNode[i_down][j] = 0
         stateChange = 1
     return NewNode, stateChange;

# TESITNG
print('MOVING TILE DOWN, IF POSSIBLE, TEST')
print(Node_State_i)
[Node_State_i, stateChange] = ActionMoveDown(Node_State_i)
print(Node_State_i)
print(stateChange)
# END TESTING

def NewNode(NewNodeIndex, NewNode, nodeStateDict):
     """Adds new node to dictionary,
        checks whether node is new or not"""
     repeat = 0
     print('START NEW NODE FUNCTION ')
     print('repeat value ' + str(repeat))
     print('new node index ' + str(NewNodeIndex))
     print('new node ' + str(NewNode))
     print('dict ' + str(nodeStateDict))
     if NewNode in nodeStateDict.values() == True:
         repeat = 1
         print('REPEAT EXISTS')
         print(repeat)
     else:
         print('NO REPEATS')
         nodeStateDict[NewNodeIndex] = NewNode
         NewNodeIndex += 1
     print(nodeStateDict)
     print(NewNodeIndex)
     print('END NEW NODE FUNCTION')
     return nodeStateDict, NewNodeIndex

# GENERATING GRAPH
print('\n===GENERATATE GRAPH===\n')
# PARAMETERS
Node_State_i = [[1, 2, 3],[4, 5, 6],[0, 7, 8]]
Node_Index_i = 1
Parent_Node_Index_i = 1
Node_Goal = [[1, 2, 3],[4, 5, 6],[7, 8, 0]]
# DICTIONARIES
# DICTIONARY THAT SAVES KEY NODE INDEX AND VALUE STATE
nodeStateDict = {}
nodeStateDict[Node_Index_i] = Node_State_i
print(nodeStateDict)
# DICTIONARY THAT SAVES KEY NODE INDEX AND VALUE PARENT NODE
parentNodeDict = {}
parentNodeDict[Node_Index_i] = Parent_Node_Index_i
print(parentNodeDict)
print('Current node state ' + str(Node_State_i) + '\n')
# TREE GRAPH
# !!! RIGHT NOW, DICTIONARY IS LINKED TO A VARIABLE THAT UPDATES, SO THE DICIONARY VALUES ARE CHANGING WITH THE VARIABLE !!!
Node_Index = Node_Index_i + 1
Node_State = Node_State_i
while Node_State_i != Node_Goal:
    print(nodeStateDict)
    print('Move left')
    [Node_State, stateChange] = ActionMoveRight(Node_State)
    if stateChange == 0:
        print('no change')
    print(Node_State)
    print(nodeStateDict)
    [nodeStateDict, Node_Index] = NewNode(Node_Index, Node_State, nodeStateDict)


    # print('Move right')
    # [Node_State_i, stateChange] = ActionMoveRight(Node_State_i)
    # if stateChange == 0:
    #     print('no change')
    # print(Node_State_i)
    # print('Move up')
    # [Node_State_i, stateChange] = ActionMoveUp(Node_State_i)
    # if stateChange == 0:
    #     print('no change')
    # print(Node_State_i)
    # print('Move down')
    # [Node_State_i, stateChange] = ActionMoveDown(Node_State_i)
    # if stateChange == 0:
    #     print('no change')
    # print(Node_State_i)
print('===END===\n\n')


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
