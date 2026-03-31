EMPTY = '.'
TREASURE = 'T'
AGENT = 'A'
WUMPUS = 'W'
PIT = 'P'
I = 'I'
J = 'J'
K = 'K'
L = 'L'
EXIT = '0'

matrix = [
    [EMPTY, TREASURE, EMPTY, PIT],
    [PIT, WUMPUS, EMPTY, PIT],
    [PIT, EMPTY, EMPTY, EMPTY],
    [AGENT, EMPTY, EMPTY, PIT]
]

def print_matrix(matrix):
    for row in matrix:
        visible_row = ['*' if cell in (EMPTY, PIT, TREASURE, WUMPUS) else cell for cell in row]
        print("\t".join(visible_row))
        print("-" * 25)
    print()

def print_available_moves(matrix, i, j):
    directions = {
        I: (-1, 0),    # UP
        K: (1, 0),     # DOWN
        J: (0, -1),    # LEFT
        L: (0, 1)      # RIGHT
    }

    available_moves = []

    for direction, (di, dj) in directions.items():
        new_i, new_j = i + di, j + dj
        if 0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[0]):
            available_moves.append(f"{direction}")

    print(f"Available Moves: {', '.join(available_moves)}")

def move_agent(matrix, direction):
    directions = {
        I: (-1, 0),    
        K: (1, 0),     
        J: (0, -1),    
        L: (0, 1)      
    }

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == AGENT:
                new_i, new_j = i + directions[direction][0], j + directions[direction][1]
                if 0 <= new_i < len(matrix) and 0 <= new_j < len(matrix[0]):
                    if matrix[new_i][new_j] == TREASURE:
                        print("Congratulations!! You found the Treasure. You Won.")
                        return True
                    elif matrix[new_i][new_j] == WUMPUS:
                        print("The Monster ate you! You Lost.")
                        return True
                    elif matrix[new_i][new_j] == PIT:
                        print("You fell into a Pit!! You Lost.")
                        return True
                    else:
                        matrix[i][j], matrix[new_i][new_j] = EMPTY, AGENT
                        return False
                else:
                    print("Invalid Move!!")
                    return True

while True:
    print_matrix(matrix)

    agent_i, agent_j = None, None
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == AGENT:
                agent_i, agent_j = i, j
                break

    print_available_moves(matrix, agent_i, agent_j)

    direction = input("Enter the direction (I, K, J, L) to move the agent, or 0 to Exit: ").upper()

    if direction in [I, J, K, L]:
        success = move_agent(matrix, direction)
        if success:
            break
    elif direction == EXIT:
        print("You Quit the Game!")
        break
    else:
        print("Invalid Move! Please refer to the direction moves.")