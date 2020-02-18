import numpy as np

# Parameters
Node_State_i = [[1, 2, 3],[4, 5, 6],[7, 8, 0]]
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
print(Node_State_i)
[i,j] = BlankTileLocation(Node_State_i)
print(i,j)
# END TESTING

# THERE'S A PROBLEM WITH PYTHON 0 BASED INDEXING AND FOLLOWING THE PROJECT SYSTEM OF 1-3
def ActionMoveLeft(CurrentNode):
    """Move tile LEFT, if possible"""
    NewNode = CurrentNode
    [i,j] = BlankTileLocation(CurrentNode)
    print(i,j)
    if j != 1:
        j_left = j - 1
        numTile = CurrentNode[i][j_left] # HERE IS THE ISSUE. PYTHON WANTS 0-2. PROJECT WANTS 1-3.
        NewNode[i][j] = numTile
        NewNode[i][j_left] = 0
    return NewNode;

# TESTING
print(Node_State_i)
Node_State_i = ActionMoveLeft(Node_State_i)
print(Node_State_i)
# END TESTING

# def [Status, NewNode] = ActionMoveRight(CurrentNode):
#     """Move tile RIGHT, if possible"""
# def [Status, NewNode] = ActionMoveUp(CurrentNode):
#     """Move tile UP, if possible"""
# def [Status, NewNode] = ActionMoveDown(CurrentNode):
#     """Move tile DOWN, if possible"""
# def [Nodes, NodesInfo] = AddNode(NewNode):
#     """Adds current node to Matrix_8puzzle_Nodes
#         Checks whether node is new or not"""
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
