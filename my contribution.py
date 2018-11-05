current_direction = direction(snek['coords'][1], snek['coords'][0])

for enemy in data['snakes']:
    if current_direction == 'left' || current_direction == 'right':
        if (len(enemy['coords']) < len(snek['coords'])-1):
            if enemy['coords'][0] == snek['coords'][1][1]+1:
                path = [(snek['coords'][0][0],snek['coords'][0][1]+1)]
            elif enemy['coords'][0] == snek['coords'][1][1]-1:
                path = [(snek['coords'][0][0],snek['coords'][0][1]-1)]
        else:
            if enemy['coords'][0] == snek['coords'][2][1]+1:
                path = [(snek['coords'][0][0],snek['coords'][0][1]+1)]
            elif enemy['coords'][0] == snek['coords'][2][1]-1:
                path = [(snek['coords'][0][0],snek['coords'][0][1]-1)]
    elif current_direction == 'up' || current_direction == 'down':
        if (len(enemy['coords']) < len(snek['coords'])-1):
            if enemy['coords'][0] == snek['coords'][1][0]+1:
                path = [(snek['coords'][0][0]+1,snek['coords'][0][1])] 
            elif enemy['coords'][0] == snek['coords'][1][0]-1:
                path = [(snek['coords'][0][0]-1,snek['coords'][0][1])]
        else:
            if enemy['coords'][0] == snek['coords'][2][0]+1:
                path = [(snek['coords'][0][0]+1,snek['coords'][0][1])]
            elif enemy['coords'][0] == snek['coords'][2][0]-1:
                path = [(snek['coords'][0][0]-1,snek['coords'][0][1])]

(only make move cut off move if can get back to tail after)