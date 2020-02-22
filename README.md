# ENPM661-Project1
### By Jaad Lepak

## Overview
Project 1 is a python script that solves the 8-matrix puzzle. The puzzle is solved by generating a tree graph and exploring each outcome as the blank tile is moved left, right, up, and down. Once the goal is reached, the script backtracks through the tree graph to reveal the steps required to solve the puzzle from start to finish. 
Here is an example of the tree graph as the blank tile is moved left, up, and right:

			2 8 3 
			1 6 4
			7 0 5
	 	    /    |     \
		2 8 3	2 8 3	2 8 3
		1 6 4	1 0 4	1 6 4
		0 7 5	7 6 5	7 5 0
	       /  |  \ /  |  \ /  |  \
	        ...      ...      ...

The tree graph is continously generated until a solution is found. This script does not check if the puzzle is solvable, so the program will continue to run until interrupted by the user.
The code is organized into the following sections:

* Input
* Functions
* Explore
* Print

## Section 1: Input

This is where the user inputs the configuration of the puzzle they would like to solve. The puzzle must be inserted in list form, arranged in column-based format. Here is an example:

	 -----------
	| 1 | 2 | 3 | 
	|-----------|
	| 4 | 5 | 6 | 
	|-----------|
	| 7 | 8 | 0 | 
	 -----------

The puzzle above in list form is:
[[1, 4, 7], [2, 5, 8], [3, 6, 0]]

The puzzle shown in the example above is also the solution that the program is looking for.

## Section 2: Functions

This section lists all the functions that Jaad has made himself. They are all used to solve the 8-matrix puzzle.

* __BlankTileLocation__ - Locates the blank tile, or '0', in the list that represents the 8-matrix puzzle. Outputs the row and column as numbers from 1 thru 3.
* __ActionMoveLeft__ - If the blank tile is NOT in the first column, it is moved to the left by switching places with the number to the left of the blank tile. Outputs the list and variable stateChange. This variable stateChange returns 0 if the left move was not possible and the puzzle remains unchanged. Otherwise, the variable returns 1.
* __ActionMoveRight__ - Similar functionality to ActionMoveLeft, but moves the blank tile to the right, as long as the blank tile is NOT in the last column.
* __ActionMoveUp__ - Similar functionality to ActionMoveLeft, but moves the blank tile up, as long as the blank tile is NOT in the first row.
* __ActionMoveDown__ - Similar functionality to ActionMoveLeft, but moves the blank tile down, as long as the blank tile is NOT in the last row.
* __list2num__ - Converts the list that represents the puzzle into a single integer. This is to improve speed as the puzzle is being solved.
* __NewNode__ - Keeps track of all moves made while solving the puzzle. While solving, if the program encounters a configuration of the puzzle that was already investigated, it ignores that configuration and does NOT log it.
* __generatePath__ - Once the puzzle is solved, this function is used to generate the steps required to solve the puzzle.
* __printPath__ - Outputs two text files to the same folder path as the python script. "nodePath.txt" only records each step to solve the puzzle from beginning to end. Each new line represents the puzzle in a column-based format, where '1 4 7 2 5 8 3 6 0' is the goal. "NodesInfo.txt" records the numbered nodes from the tree graph that relate to the solving path. The first column contains the child nodes and the second column contains the parent nodes.
* __printNode__ - Outputs a text file that captures all the puzzle states explored while generating the tree graph. Each new line represents the puzzle in a column-based format, where '1 4 7 2 5 8 3 6 0' is the goal.


## Section 3: Explore

This section moves the blank tile around in the puzzle and generates an abstract version of the tree graph described in the overview. Each puzzle state explored is stored in "Nodes.txt". In this file, each new line represents the puzzle in a column-based format, where '1 4 7 2 5 8 3 6 0' is the goal. The script continues to search for a solution and only stops if a solution is found or the user interrupts the program. Some messages are printed to help with visibility. Here is an example if the program is successful:

	NOW SOLVING FOR
	[[[1, 0, 7], [8, 4, 6], [2, 3, 5]]]

	Calculating...

	Still Calculating...

	Still Calculating...

	SUCCESS!
	
	Start Node
	-------------
	| 1 | 8 | 2 | 
	-------------
	| 0 | 4 | 3 | 
	-------------
	| 7 | 6 | 5 | 
	-------------


	Step  1
	-------------
	| 1 | 8 | 2 | 
	-------------
	| 4 | 0 | 3 | 
	-------------
	| 7 | 6 | 5 | 
	-------------


	Step  2
	-------------
	| 1 | 0 | 2 | 
	-------------
	| 4 | 8 | 3 | 
	-------------
	| 7 | 6 | 5 | 
	-------------


	Step  3
	-------------
	| 1 | 2 | 0 | 
	-------------
	| 4 | 8 | 3 | 
	-------------
	| 7 | 6 | 5 | 
	-------------


	Step  4
	-------------
	| 1 | 2 | 3 | 
	-------------
	| 4 | 8 | 0 | 
	-------------
	| 7 | 6 | 5 | 
	-------------


	Step  5
	-------------
	| 1 | 2 | 3 | 
	-------------
	| 4 | 8 | 5 | 
	-------------
	| 7 | 6 | 0 | 
	-------------


	Step  6
	-------------
	| 1 | 2 | 3 | 
	-------------
	| 4 | 8 | 5 | 
	-------------
	| 7 | 0 | 6 | 
	-------------


	Step  7
	-------------
	| 1 | 2 | 3 | 
	-------------
	| 4 | 0 | 5 | 
	-------------
	| 7 | 8 | 6 | 
	-------------


	Step  8
	-------------
	| 1 | 2 | 3 | 
	-------------
	| 4 | 5 | 0 | 
	-------------
	| 7 | 8 | 6 | 
	-------------


	Step  9
	-------------
	| 1 | 2 | 3 | 
	-------------
	| 4 | 5 | 6 | 
	-------------
	| 7 | 8 | 0 | 
	-------------


	Achieved Goal Node
	-------------
	| 1 | 2 | 3 | 
	-------------
	| 4 | 5 | 6 | 
	-------------
	| 7 | 8 | 0 | 
	-------------

Here is an example if the program is trying to solve a potentially unsolvable puzzle and interrupted by the user:

	NOW SOLVING FOR
	[[[1, 5, 7], [8, 4, 6], [2, 3, 0]]]

	Calculating...

	Still Calculating...

	Still Calculating...

	Still Calculating...

	Still Calculating...

	Still Calculating...

	Puzzle may be unsolvable...

	Still Calculating...

	Still Calculating...

	Still Calculating...

	Still Calculating...

	Still Calculating...

	Puzzle may be unsolvable...

	Traceback (most recent call last):
	  File "C:\umd\enpm661\project1\proj1_Jaad_Lepak.py", line 250, in <module>
		Parent_Node_Index_i, counter, indexCounter, parentCounter)
	  File "C:\umd\enpm661\project1\proj1_Jaad_Lepak.py", line 132, in NewNode
		printNode(newNode)
	  File "C:\umd\enpm661\project1\proj1_Jaad_Lepak.py", line 182, in printNode
		nodeFile.close()
	KeyboardInterrupt

As the code searches, the message "Puzzle may be unsolvable" is occasionally printed to allow the user to feel comfortable interrupting the program on their own.

## Section 4: Print

When a solution is found, the path from the beginning to the end is printed in two ways.

1. The path from the abstract tree graph is captured in two text (.txt) files. "nodePath.txt" only records each step to solve the puzzle from beginning to end. Each new line represents the puzzle in a column-based format, where '1 4 7 2 5 8 3 6 0' is the goal. "NodesInfo.txt" records the numbered nodes from the tree graph that relate to the solving path. The first column contains the child nodes and the second column contains the parent nodes.
2. The final path is expressed in a more visual-friendly way in the command line using the function print_matrix. The code for this printing method was provided by "plot_path.py" and has been copied into this script. 
