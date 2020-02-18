import numpy as np

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
    NewNode = CurrentNode
    [i,j] = BlankTileLocation(CurrentNode)
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

def ActionMoveRight(CurrentNode):
    """Move tile RIGHT, if possible"""
    NewNode = CurrentNode
    [i,j] = BlankTileLocation(CurrentNode)
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

def ActionMoveUp(CurrentNode):
     """Move tile UP, if possible"""
     NewNode = CurrentNode
     [i,j] = BlankTileLocation(CurrentNode)
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

def ActionMoveDown(CurrentNode):
     """Move tile DOWN, if possible"""
     NewNode = CurrentNode
     [i,j] = BlankTileLocation(CurrentNode)
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

# ===START===

# ---Get the initial node from the user---
Node_State_i = [[1, 2, 3],[4, 5, 6],[0, 7, 8]]

print('initial node state')
print(Node_State_i)

# ---Save node information using a dictionary---
# Key is node number and Value is a tuple of node state and parent node
NodeStateDict = dict()
Node_Index_i = 1
Parent_Node_Index_i = 1
NodeStateDict[Node_Index_i] = (Node_State_i, Parent_Node_Index_i)

print('initial dictionary')
print(NodeStateDict)

# ---Apply actions to blank tile to generate new nodes---
ParentNode = Node_Index_i
NodeIndex = ParentNode
NodeState = Node_State_i.copy()

# Move left

print('parent node')
print(ParentNode)
print('node index')
print(NodeIndex)
print('MOVE LEFT')

[NewNodeState1, stateChange] = ActionMoveLeft(NodeState)

print('new node state1')
print(NewNodeState1)
print('state change')
print(stateChange)

if stateChange == 1:
# ---Check if node already exists in the data structure and add to dictionary---
    repeat = 0
    for value in NodeStateDict:
        if value == NewNodeState1:
            repeat = 1

    if repeat == 0:
        NodeIndex += 1
        NodeStateDict[NodeIndex] = (NewNodeState1, ParentNode)

    print('repeat')
    print(repeat)

print('new dictionary')
print(NodeStateDict)

# Move right

print('parent node')
print(ParentNode)
print('node index')
print(NodeIndex)
print('MOVE RIGHT')

[NewNodeState2, stateChange] = ActionMoveRight(NodeState.copy())

print('new node state2')
print(NewNodeState2)
print('state change')
print(stateChange)

if stateChange == 1:
    NodeIndex += 1
    repeat = 0
    for value in NodeStateDict:
        if value == NewNodeState2:
            repeat = 1

    if repeat == 0:
        NodeIndex += 1
        NodeStateDict[NodeIndex] = (NewNodeState2, ParentNode)

    print('repeat')
    print(repeat)

print('new dictionary') #DICTIONARY IS UPDATING PREVIOUS ENTRIES WITH THE NEW ONE INSTEAD OF LEAVING IT ALONE...
print(NodeStateDict)

# Move up
[NewNodeState, stateChange] = ActionMoveUp(NodeState)

# Move down
[NewNodeState, stateChange] = ActionMoveDown(NodeState)




# ---Check if the new node meets the goal node---

# ---Back track to find the path---

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
