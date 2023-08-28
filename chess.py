import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 800
BOARD_SIZE = 8
SQUARE_SIZE = WIDTH // BOARD_SIZE
WHITE = (255, 255, 255)
LIGHT_BLACK = (100, 100, 100)
RED = (255, 0, 0)
# Create the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")

# Load images for pieces
pieces_images = {
    'r': pygame.image.load("C:\\Users\\Dell\\OneDrive\\Desktop\\chess\\pieces\\black_rook.png"),
    'n': pygame.image.load("C:\\Users\\Dell\\OneDrive\\Desktop\\chess\\pieces\\black_knight.png"),
    'b': pygame.image.load("C:\\Users\\Dell\\OneDrive\\Desktop\\chess\\pieces\\black_bishop.png"),
    'q': pygame.image.load("C:\\Users\\Dell\\OneDrive\\Desktop\\chess\\pieces\\black_queen.png"),
    'k': pygame.image.load("C:\\Users\\Dell\\OneDrive\\Desktop\\chess\\pieces\\black_king.png"),
    'p': pygame.image.load("C:\\Users\\Dell\\OneDrive\\Desktop\\chess\\pieces\\black_pawn.png"),
    'R': pygame.image.load("C:\\Users\\Dell\\OneDrive\\Desktop\\chess\\pieces\\white_rook.png"),
    'N': pygame.image.load("C:\\Users\\Dell\\OneDrive\\Desktop\\chess\\pieces\\white_knight.png"),
    'B': pygame.image.load("C:\\Users\\Dell\\OneDrive\\Desktop\\chess\\pieces\\white_bishop.png"),
    'Q': pygame.image.load("C:\\Users\\Dell\\OneDrive\\Desktop\\chess\\pieces\\white_queen.png"),
    'K': pygame.image.load("C:\\Users\\Dell\\OneDrive\\Desktop\\chess\\pieces\\white_king.png"),
    'P': pygame.image.load("C:\\Users\\Dell\\OneDrive\\Desktop\\chess\\pieces\\white_pawn.png")
}

# Initialize the board
board = [
    ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
    ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.'],
    ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
    ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
]

def draw_board():
    for row in range(BOARD_SIZE):
        for col in range(BOARD_SIZE):
            color = WHITE if (row + col) % 2 == 0 else LIGHT_BLACK
            pygame.draw.rect(screen, color, pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            piece = board[row][col]
            if piece != '.':
                screen.blit(pieces_images[piece], pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
            
            # Draw row and column labels
            if col == 0:
                label_font = pygame.font.Font(None, 36)
                row_label = str(BOARD_SIZE - row)
                label_surface = label_font.render(row_label, True, RED)
                screen.blit(label_surface, (col * SQUARE_SIZE + 10, row * SQUARE_SIZE + SQUARE_SIZE // 2 - 20))
            if col == 7:
                label_font = pygame.font.Font(None, 36)
                row_label = str(BOARD_SIZE - row)
                label_surface = label_font.render(row_label, True, RED)
                screen.blit(label_surface, (col * SQUARE_SIZE + 10, row * SQUARE_SIZE + SQUARE_SIZE // 2 - 20))
            if row == BOARD_SIZE - 1:
                label_font = pygame.font.Font(None, 36)
                col_label = chr(ord('a') + col)
                label_surface = label_font.render(col_label, True, RED)
                screen.blit(label_surface, (col * SQUARE_SIZE + SQUARE_SIZE // 2 - 10, row * SQUARE_SIZE + SQUARE_SIZE - 30))
            if row == 0:
                label_font = pygame.font.Font(None, 36)
                col_label = chr(ord('a') + col)
                label_surface = label_font.render(col_label, True, RED)
                screen.blit(label_surface, (col * SQUARE_SIZE + SQUARE_SIZE // 2 - 10, row * SQUARE_SIZE + SQUARE_SIZE - 30))
def get_clicked_position(pos):
    col = pos[0] // SQUARE_SIZE
    row = pos[1] // SQUARE_SIZE
    return row, col



selected_piece = None
selected_position = None
def is_valid_move(start_pos, end_pos,move_counter):
    start_row, start_col = start_pos
    end_row, end_col = end_pos
    piece = board[start_row][start_col]
    destination = board[end_row][end_col]

    # Check if the destination sqare is occupied by a piece of the same color
    if destination != '.' and piece.islower() == destination.islower():
        return False

   #pieces movement 
    if piece == 'P' and move_counter%2!=0:
        
        if start_col == end_col and start_row==6 and abs(end_row - start_row) in [1, 2] :
            return True
        elif start_col == end_col and abs(end_row - start_row)==1 :
            return True
        elif abs(end_col - start_col) ==1 and abs(end_row - start_row)==1 and destination in ['p','n','q','r','b']:
            return True
    elif piece == 'p' and move_counter%2==0:
        
        if start_col == end_col and start_row==1 and abs(end_row - start_row) in [1, 2] :
            return True
        elif start_col == end_col and abs(end_row - start_row)==1 :
            return True
        elif abs(end_col - start_col) ==1 and abs(end_row - start_row)==1 and destination in ['P','N','Q','R','B']:
            return True
    
    elif piece == 'R' and move_counter%2!=0:
        if start_row != end_row and start_col != end_col:
            return False
    
        # Check for obstacles along the path
        row_direction = 0 if start_row == end_row else (1 if end_row > start_row else -1)
        col_direction = 0 if start_col == end_col else (1 if end_col > start_col else -1)

        row = start_row + row_direction
        col = start_col + col_direction

        while row != end_row or col != end_col:
            if board[row][col] != '.':
                return False  # Obstacle on the way

            row += row_direction
            col += col_direction

        return True
    elif piece == 'r' and move_counter%2==0:
        if start_row != end_row and start_col != end_col:
            return False
    
        # Check for obstacles along the path
        row_direction = 0 if start_row == end_row else (1 if end_row > start_row else -1)
        col_direction = 0 if start_col == end_col else (1 if end_col > start_col else -1)

        row = start_row + row_direction
        col = start_col + col_direction

        while row != end_row or col != end_col:
            if board[row][col] != '.':
                return False  # Obstacle on the way

            row += row_direction
            col += col_direction

        return True

    elif piece == 'N' and move_counter%2!=0:
        # Knight movement rules (L-shape)
        if (abs(end_row - start_row) == 2 and abs(end_col - start_col) == 1) or \
           (abs(end_row - start_row) == 1 and abs(end_col - start_col) == 2):
            return True
    elif piece == 'n' and move_counter%2==0:
        # Knight movement rules (L-shape)
        if (abs(end_row - start_row) == 2 and abs(end_col - start_col) == 1) or \
           (abs(end_row - start_row) == 1 and abs(end_col - start_col) == 2):
            return True
    elif piece =='B'  and move_counter%2!=0:
        if (abs(end_row - start_row) == abs(end_col - start_col)):
            return True
    elif piece =='b'  and move_counter%2==0:
        if (abs(end_row - start_row) == abs(end_col - start_col)):
            return True
    elif piece=='Q' and move_counter%2!=0:
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        return row_diff == col_diff or start_row == end_row or start_col == end_col
    elif piece=='q' and move_counter%2==0:
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        return row_diff == col_diff or start_row == end_row or start_col == end_col  
    elif piece =='K'and move_counter%2!=0:
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        # Check if it's a king-side castling for white or black
        king_side = (end_col - start_col) == 2
        rook_col = 7 if king_side else 0

        # Ensure the king and rook have not moved
        if board[start_row][start_col] == 'K' and board[start_row][rook_col] == 'R':
            
            # Check if there are no pieces between king and rook
            for col in range(start_col + 1, rook_col):
                if board[start_row][col] != '.':
                    return False
            if rook_col==7:
                # Update the board for castling
                board[start_row][start_col + 2] = 'K'
                board[start_row][start_col] = '.'
                board[start_row][rook_col - 2] = 'R'
                board[start_row][rook_col] = '.'
            else:
                board[start_row][start_col - 2] = 'K'
                board[start_row][start_col] = '.'
                board[start_row][rook_col + 3] = 'R'
                board[start_row][rook_col] = '.'
            return True
        else:
            row_diff = abs(end_row - start_row)
            col_diff = abs(end_col - start_col)
            return row_diff <= 1 and col_diff <= 1
        
    elif piece =='k'and move_counter%2==0:
        row_diff = abs(end_row - start_row)
        col_diff = abs(end_col - start_col)
        return row_diff <= 1 and col_diff <= 1
    return False
dragging = False
dragged_piece = None
offset_x = 0
offset_y = 0
move_counter = 1  # Initialize the move counter

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            clicked_position = get_clicked_position(pygame.mouse.get_pos())
            row, col = clicked_position
            piece = board[row][col]

            if piece != '.':
                dragging = True
                dragged_piece = piece
                offset_x = col * SQUARE_SIZE - pygame.mouse.get_pos()[0]
                offset_y = row * SQUARE_SIZE - pygame.mouse.get_pos()[1]
                selected_position = clicked_position

        if event.type == pygame.MOUSEBUTTONUP:
            if dragging:
                dragging = False
                row, col = get_clicked_position(pygame.mouse.get_pos())
                if is_valid_move(selected_position, (row, col),move_counter):
                    if piece=='P' and row==0:
                        choice=input('Enter your choise ')
                        if choice=='Q':
                            dragged_piece='Q'
                        elif choice=='N':
                            dragged_piece='N'
                        elif choice=='R':
                            dragged_piece='R'
                        elif choice=='B':
                            dragged_piece='B'
                    if piece=='p' and row==7:
                        choice=input('Enter your choise ')
                        if choice=='q':
                            dragged_piece='q'
                        elif choice=='n':
                            dragged_piece='n'
                        elif choice=='r':
                            dragged_piece='r'
                        elif choice=='b':
                            dragged_piece='b'
                    board[row][col] = dragged_piece
                    row_start, col_start = selected_position
                    board[row_start][col_start] = '.'

                    move_counter += 1  # Increment the move counter

                dragged_piece = None
                selected_position = None

    if dragging and dragged_piece is not None:
        x, y = pygame.mouse.get_pos()
        x += offset_x
        y += offset_y
        screen.blit(pieces_images[dragged_piece], pygame.Rect(x, y, SQUARE_SIZE, SQUARE_SIZE))

    draw_board()
    pygame.display.flip()


