import numpy as np
import random
m = 3
matrix = [[0 for j in range(m)] for i in range(m)]
def isSafe(matrix,i,j):
    if matrix[i][j] == 0:
        return True
    else:
        return False
def safeRow(matrix,i,m,c):
    for x in range(m):
        if matrix[i][x] == c:
            return False
    return True
def safeColumn(matrix,j,m,c):
    for x in range(m):
        if matrix[x][j] == c:
            return False
    return True
def safeRightDiagonal(matrix,m,c):
    for x in range(m):
        if matrix[x][x] == c:
            return False
    return True
def safeLeftDiagonal(matrix,m,c):
    j = m-1
    for x in range(m):
        if matrix[x][j] == c:
            return False
        j = j-1
    return True
def isdiagonalEntry(i,j,m):
    if i == j:
        return True
    elif i == 0 and j == m-1:
        return True
    elif i == m-1 and j == 0:
        return True
    else:
        return False
    
def isGameOver(m,c):
    for x in range(m):
        for y in range(m):
            if isdiagonalEntry(x,y,m):
                if safeRightDiagonal(matrix,m,c):
                    return False
                elif safeLeftDiagonal(matrix,m,c):
                    return False
                elif safeColumn(matrix,y,m,c):
                    return False
                elif safeRow(matrix,x,m,c):
                    return False
                else:
                    return True
            else:
                if safeColumn(matrix,y,m,c):
                    return False
                elif safeRow(matrix,x,m,c):
                    return False
                else:
                    return True
def checkspace(i,j,m,matrix,ch):
    if ch == 'c':
        for x in range(m):
            if matrix[x][j] == 0:
                return True, x, j
        return False
    elif ch == 'r':
        for x in range(m):
            if matrix[i][x] == 0:
                return True, i, x
        return False
    elif ch == 'rd':
        for x in range(m):
            if matrix[x][x] == 0:
                return True, x, x
        return False
    elif ch == 'ld':
        z = m-1
        for x in range(m):
            if matrix[x][z] == 0:
                return True, x, z
            z = z-1
        return False
def showboard(matrix,m):
    for x in range(m):
        for y in range(m):
            print(matrix[x][y],"   ",end="")
        print('\n')
def isboardfull(matrix,m):
    for x in range(m):
        for y in range(m):
            if matrix[x][y] == 0:
                return False
    return True
def winchance(matrix,i,j,m,ch,w):
    if w == 'c':
        for x in range(m):
            if matrix[x][j] != ch:
                return False
        return True
    elif w == 'r':
        for x in range(m):
            if matrix[i][x] != ch:
                return False
        return True
    elif w == 'rd':
        for x in range(m):
            if matrix[x][x] != ch:
                return False
        return True
    elif w == 'ld':
        z = m-1
        for x in range(m):
            if matrix[x][z] != ch:
                return False
            z = z-1
        return True
    
def isWin(matrix,m,ch):
    for i in range(m):
        for j in range(m):
            if isdiagonalEntry(i,j,m):
                if winchance(matrix,i,j,m,ch,'rd'):
                    return True
                elif winchance(matrix,i,j,m,ch,'ld'):
                    return True
                elif winchance(matrix,i,j,m,ch,'c'):
                    return True
                elif winchance(matrix,i,j,m,ch,'r'):
                    return True
            else:
                if winchance(matrix,i,j,m,ch,'c'):
                    return True
                elif winchance(matrix,i,j,m,ch,'r'):
                    return True
    return False        
            
def tictactoe():
    while not isboardfull(matrix,m):
        for i in range(m):
            con = False
            for j in range(m):
                if isdiagonalEntry(i,j,m):
                    if safeRightDiagonal(matrix,m,'U') and checkspace(i,j,m,matrix,'rd')[0]:
                        matrix[checkspace(i,j,m,matrix,'rd')[1]][checkspace(i,j,m,matrix,'rd')[2]]='C'
                        con = True
                        break
                    elif safeLeftDiagonal(matrix,m,'U') and checkspace(i,j,m,matrix,'ld')[0]:
                        matrix[checkspace(i,j,m,matrix,'ld')[1]][checkspace(i,j,m,matrix,'ld')[2]]='C'
                        con = True
                        break
                    elif safeColumn(matrix,j,m,'U') and checkspace(i,j,m,matrix,'c')[0]:
                        matrix[checkspace(i,j,m,matrix,'c')[1]][checkspace(i,j,m,matrix,'c')[2]]='C'
                        con = True
                        break
                    elif safeRow(matrix,i,m,'U') and checkspace(i,j,m,matrix,'r')[0]:
                        matrix[checkspace(i,j,m,matrix,'r')[1]][checkspace(i,j,m,matrix,'r')[2]]='C'
                        con = True
                        break
                else:
                    if safeColumn(matrix,j,m,'U') and checkspace(i,j,m,matrix,'c')[0]:
                        matrix[checkspace(i,j,m,matrix,'c')[1]][checkspace(i,j,m,matrix,'c')[2]]='C'
                        con = True
                        break
                    elif safeRow(matrix,i,m,'U') and checkspace(i,j,m,matrix,'r')[0]:
                        matrix[checkspace(i,j,m,matrix,'r')[1]][checkspace(i,j,m,matrix,'r')[2]]='C'
                        con = True
                        break
            if con == True:
                print('After Computers turn :')
                print("\n")
                showboard(matrix,m)
                print("\n")
                print("\n")
                break
        if isWin(matrix,m,'C'):
            print("\n")
            print("GAME OVER !!!!!")
            print("\n")
            print("Result : Computer Wins")
            break
        c = True
        while c:
            x = int(input('Enter x:'))
            y = int(input('Enter y:'))
            if x <0 or x>=m or y <0 or y>=m:
                print('Invalid index')
                print('\n')
            elif matrix[x][y] != 0:
                print('Already marked')
                print('\n')
            else:
                c = False
        matrix[x][y]='U'
        print('After Yours turn :')
        print("\n")
        showboard(matrix,m)
        print("\n")
        print("\n")
        if isWin(matrix,m,'U'):
            print("\n")
            print("GAME OVER !!!!!")
            print("\n")
            print("Result : You Wins")
            break

                    
tictactoe()      
                    
                    
                