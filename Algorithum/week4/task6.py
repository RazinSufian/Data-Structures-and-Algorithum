
##mine:
from collections import deque
inpt = open("f:\Codeing\Algorithum\week4\input6.txt", "r")
oupt = open("f:\Codeing\Algorithum\week4\output6.txt", "w")
data_into_list = inpt.readlines()
R, H = map(int, data_into_list[0].split())
grid = [list(line.strip()) for line in data_into_list[1:R+1]]
#print(grid)

total_elemnts=R*H

def flood_fill(grid,start_row,start_col):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    queue=deque([(start_row, start_col)])
    diamond_count=0
    check_elemts=0
    while queue:
        row,col=queue.popleft()

        if grid[row][col]=="D":
            diamond_count+=1
        grid[row][col]="x"
        check_elemts+=1

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col]!="x" and grid[new_row][new_col]!="#":
                queue.append((new_row, new_col))
        
        
    return check_elemts,diamond_count
        


max_diamonds=0
for i in range(R):
    if total_elemnts==0:
        #print("in")
        break
    for j in range(H):

        if grid[i][j]== "#":
            grid[i][j]="x"
            total_elemnts-=1
        elif grid[i][j]=="x":
            pass
        else:
            elements_checked,diamonds_found=flood_fill(grid,i, j)
            #print(diamonds_found)
            total_elemnts-=elements_checked
            max_diamonds=max(max_diamonds,diamonds_found)
            pass
#print(grid)
print(max_diamonds)
