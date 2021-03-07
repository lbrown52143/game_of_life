#Name: Lamar Brown
#Game of Life

import random

def build_board_random(row, col):
	a = [[ 0 for i in range(col)] for j in range(row)] 
	for i in range(row):
		for j in range(col):
			a[i][j]=random.randint(0, 1)

	return a

def build_board_user(row, col):
	a = [[ 0 for i in range(col)] for j in range(row)] 
	for i in range(row):
		for j in range(col):
			a[i][j]=int(input("Enter 0 or 1 to fill the board. "))

	return a


def printBoard(board, row, col):
	for i in range(row):
		print(board[i])


def copyBoard(board, row, col):
        b = [[ 0 for i in range(col)] for j in range(row)] 
        for i in range(row):
                for j in range(col):
                        b[i][j]=board[i][j]

        return b


def change(oldBoard, newBoard, row, col):
	change_count=0
	for i in range(row):
		for j in range(col):
			if(newBoard[i][j]!=oldBoard[i][j]):
				change_count+=1


	return change_count


def count(board, row, col):
	count_life=0
	for i in range(row):
		for j in range(col):
			if(board[i][j]==1):
				count_life+=1

	return count_life

def neigh(board, row, col, i, j):
#No loops, just long if-else statement
	sum=0
	new_num=0
	if(i==0 and j==0):
		#upper left corner
		sum=board[i][j+1]+board[i+1][j]+board[i+1][j+1]
		if(board[i][j]==0):
			if(sum==3):
				new_num+=1
		elif(board[i][j]==1):
			if(sum==2 or sum==3):
				new_num+=1
			elif(sum<2):
				new_num+=0
			elif(sum>3):
				new_num+=0

	elif(i==row-1 and j==0):
	        #bottom left corner
		sum=board[i][j+1]+board[i-1][j]+board[i-1][j+1]
		if(board[i][j]==0):
			if(sum==3):
				new_num+=1
		elif(board[i][j]==1):
			if(sum==2 or sum==3):
				new_num+=1
			elif(sum<2):
				new_num+=0
			elif(sum>3):
				new_num+=0

	elif(i==0 and j==col-1):
		#upper right corner
		sum=board[i][j-1]+board[i+1][j-1]+board[i+1][j]
		if(board[i][j]==0):
			if(sum==3):
				new_num+=1
		elif(board[i][j]==1):
			if(sum==2 or sum==3):
				new_num+=1
			elif(sum<2):
				new_num+=0
			elif(sum>3):
				new_num+=0


	elif(i==row-1 and j==col-1):
		#bottom right corner
		sum=board[i][j-1]+board[i-1][j]+board[i-1][j-1]
		if(board[i][j]==0):
			if(sum==3):
				new_num+=1
		elif(board[i][j]==1):
			if(sum==2 or sum==3):
				new_num+=1
			elif(sum<2):
				new_num+=0
			elif(sum>3):
				new_num+=0


	elif(i==0):
		#first row except corners
		sum=board[i][j-1]+board[i+1][j-1]+board[i+1][j]+board[i+1][j+1]+board[i][j+1]
		if(board[i][j]==0):
			if(sum==3):
				new_num+=1
		elif(board[i][j]==1):
			if(sum==2 or sum==3):
				new_num+=1
			elif(sum<2):
				new_num+=0
			elif(sum>3):
				new_num+=0


	elif(i==row-1):
		#last row except corners
		sum=board[i-1][j-1]+board[i-1][j]+board[i-1][j+1]+board[i][j-1]+board[i][j+1]
		if(board[i][j]==0):
			if(sum==3):
				new_num+=1
		elif(board[i][j]==1):
			if(sum==2 or sum==3):
				new_num+=1
			elif(sum<2):
				new_num+=0
			elif(sum>3):
				new_num+=0


	elif(j==0):
		#first column except corners
		sum=board[i-1][j]+board[i-1][j+1]+board[i][j+1]+board[i+1][j+1]+board[i+1][j]
		if(board[i][j]==0):
			if(sum==3):
				new_num+=1
		elif(board[i][j]==1):
			if(sum==2 or sum==3):
				new_num+=1
			elif(sum<2):
				new_num+=0
			elif(sum>3):
				new_num+=0


	elif(j==col-1):
		#last column except corners
		sum=board[i-1][j]+board[i-1][j-1]+board[i][j-1]+board[i+1][j-1]+board[i+1][j]
		if(board[i][j]==0):
			if(sum==3):
				new_num+=1
		elif(board[i][j]==1):
			if(sum==2 or sum==3):
				new_num+=1
			elif(sum<2):
				new_num+=0
			elif(sum>3):
				new_num+=0


	else:
		#middle item except corners
		sum=board[i-1][j-1]+board[i-1][j]+board[i-1][j+1]+board[i][j+1]+board[i+1][j+1]+board[i+1][j]+board[i+1][j-1]+board[i][j-1]
		if(board[i][j]==0):
			if(sum==3):
				new_num+=1
		elif(board[i][j]==1):
			if(sum==2 or sum==3):
				new_num+=1
			elif(sum<2):
				new_num+=0
			elif(sum>3):
				new_num+=0


	return new_num, sum


def all_neigh(board, row, col):
	a = [[ 0 for i in range(col)] for j in range(row)]
	for i in range(row):
		for j in range(col):
			board_num, sum=neigh(board, row, col, i, j)
			a[i][j]=sum

	return a

def play_game(board, row, col, max_time):
	i=0
	reach_max_time=True
	while(i!=max_time):
		new_board=make_new_board(board, row, col)
		print("Time", i+1)
		printBoard(new_board, row, col)

		change_count=change(board, new_board, row, col)
		if(change_count>0):
			board=copyBoard(new_board, row, col)
			i+=1
		else:
			reach_max_time=False
			i=max_time 


	if(reach_max_time):
		result=True
	else:
		result=False

	return new_board, result


def make_new_board(board, row, col):
	a=[[ 0 for i in range(col)] for j in range(row)]
	for i in range(row):
		for j in range(col):
			new_num, sum=neigh(board, row, col, i , j)
			a[i][j]=new_num

	return a
	

def endMessage(status):
	if(status==True):
		print("The game was completed at the maximum number of configurations.")
	else:
		print("The game was completed before the maximum number of configurations.")


def main():
	choice=int(input("Enter 0 for user input or enter 1 for random input. "))
	max_time=int(input("What is the max amount of times the board will change? "))
	row=random.randint(3,5)
	col=random.randint(3,5)

	if(choice==0):
		board=build_board_user(row, col)
		print("Time T")
		printBoard(board, row, col)
	else:
		board=build_board_random(row, col)
		print("Time T")
		printBoard(board, row, col)

#	board_copy=copyBoard(board, row, col)
#	print("Testing copyBoard function")
#	printBoard(board_copy, row, col)
#	print("testing changeBoard")

	
	new_board, status=play_game(board, row, col, max_time)

	print("")
	print("After the final change in the board,")

	counter=count(new_board, row, col)
	print("The number of people in the neighborhood is",counter)

	neigh_list=all_neigh(new_board, row, col)
	print("Printing number of neighbors for each location")
	printBoard(neigh_list, row, col)

	endMessage(status)

main()
