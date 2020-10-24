def turtle(coord, direction):
    cur_coord = list(coord)
    cur_direction = direction
    command = ""
    while True:
        command = yield cur_coord
        #print(command)
        if command == 'f':
            if cur_direction == 0:
                cur_coord[0] += 1
            elif cur_direction == 1:
                cur_coord[1] += 1
            elif cur_direction == 2:
                cur_coord[0] -= 1
            else:
                cur_coord[1] -= 1
        elif command == 'l':
            cur_direction = (cur_direction + 1) % 4
        else:
            cur_direction = (cur_direction - 1) % 4
        #print(cur_direction)
        #print(cur_coord[0], cur_coord[1])
        
#robo = turtle((0,0),0)
#start = next(robo)
#for c in "flfrffrffr":
    #print(*robo.send(c))