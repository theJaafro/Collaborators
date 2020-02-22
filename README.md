# ENPM661-Project1
ENPM661-Project1
================
By Jaad Lepak
-------------

---

Overview
--------

Project 1 is a python script that solves the 8-matrix puzzle. The puzzle is solved by generating a tree graph and exploring each outcome as the blank tile is moved left, right, up, and down. Once the goal is reached, the script backtracks through the tree graph to reveal the steps required to solve the puzzle from start to finish. 
Here is an example of the tree graph as the blank tile is moved left, up, and right:

				2 8 3 
				1 6 4
				7 0 5
			  /   |    \
		2 8 3	2 8 3	2 8 3
		1 6 4	1 0 4	1 6 4
		0 7 5	7 6 5	7 5 0
		
		...		...		...

The tree graph is continously generated until a solution is found. This script does not check if the puzzle is solvable, so the program will continue to run until interrupted by the user.
The code is organized into three sections:

	* Functions
	* Explore
	* Print

Section 1: Functions
--------------------

This section lists all the functions that Jaad has made himself. They are all used to solve the 8-matrix puzzle.

	* BlankTileLocation - Locates the blank tile, or '0', in the list that represents the 8-matrix puzzle. Outputs the row and column as numbers from 1 thru 3.
	* ActionMoveLeft - If the blank tile is NOT in the first column, it is moved to the left by switching places with the number to the left of the blank tile. Outputs the list and variable stateChange. This variable stateChange returns 0 if the left move was not possible and the puzzle remains unchanged. Otherwise, the variable returns 1.
	* ActionMoveRight - Similar functionality to ActionMoveLeft, but moves the blank tile to the right, as long as the blank tile is NOT in the last column.
	* ActionMoveUp - Similar functionality to ActionMoveLeft, but moves the blank tile up, as long as the blank tile is NOT in the first row.
	* ActionMoveDown - Similar functionality to ActionMoveLeft, but moves the blank tile down, as long as the blank tile is NOT in the last row.
	* list2num - Converts the list that represents the puzzle into a single integer. This is to improve speed as the puzzle is being solved.
	* NewNode - Keeps track of all moves made while solving the puzzle. While solving, if the program encounters a configuration of the puzzle that was already investigated, it ignores that configuration and does NOT log it.
	* generatePath - Once the puzzle is solved, this function is used to generate the steps required to solve the puzzle.
	* printPath - Outputs two text files to the same folder path as the python script. "nodePath.txt" only records each step to solve the puzzle from beginning to end. Each new line represents the puzzle in a column-based format, where '1 4 7 2 5 8 3 6 0' is the goal. "NodesInfo.txt" records the numbered nodes from the tree graph that relate to the solving path. The first column contains the child nodes and the second column contains the parent nodes.
	* printNode - Outputs a text file that captures all the puzzle states explored while generating the tree graph. Each new line represents the puzzle in a column-based format, where '1 4 7 2 5 8 3 6 0' is the goal.
	

Section 2: Explore
------------------