# Author: Chris Hauser
# Date: 6/4/2020
# Description: A program which creates an instance of Gess and allows users to manipulate pieces on the board until
# a winner is found. There exists classes for the game instance and the pieces a user attempts to create when making
# a move.


class GessGame:
    """Represents an instance of the Gess board game. Tracks the state of the board and game state as well as current
    player. Is able to take in and complete all player commands to move pieces or resign. Contains a method to print
    the current board state. This class passes itself to create a Piece object when make_move is called. This class
    handles the legality of a given move once the move has begun and resolves any outcomes of making a move."""

    def __init__(self):
        """Creates a GessGame instance with an unfinished game state, a starting board layout, and black as the
        current player."""
        self._game_state = 'UNFINISHED'
        self._player = 'B'
        self._board = [
            # a    b    c    d    e    f    g    h    i    j    k    l    m    n    o    p    q    r    s    t
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],  # 20
            ['-', '-', 'W', '-', 'W', '-', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', '-', 'W', '-', 'W', '-', '-'],  # 19
            ['-', 'W', 'W', 'W', '-', 'W', '-', 'W', 'W', 'W', 'W', '-', 'W', '-', 'W', '-', 'W', 'W', 'W', '-'],  # 18
            ['-', '-', 'W', '-', 'W', '-', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', '-', 'W', '-', 'W', '-', '-'],  # 17
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],  # 16
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],  # 15
            ['-', '-', 'W', '-', '-', 'W', '-', '-', 'W', '-', '-', 'W', '-', '-', 'W', '-', '-', 'W', '-', '-'],  # 14
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],  # 13
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],  # 12
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],  # 11
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],  # 10
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],  # 9
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],  # 8
            ['-', '-', 'B', '-', '-', 'B', '-', '-', 'B', '-', '-', 'B', '-', '-', 'B', '-', '-', 'B', '-', '-'],  # 7
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],  # 6
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-'],  # 5
            ['-', '-', 'B', '-', 'B', '-', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', '-', 'B', '-', 'B', '-', '-'],  # 4
            ['-', 'B', 'B', 'B', '-', 'B', '-', 'B', 'B', 'B', 'B', '-', 'B', '-', 'B', '-', 'B', 'B', 'B', '-'],  # 3
            ['-', '-', 'B', '-', 'B', '-', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', '-', 'B', '-', 'B', '-', '-'],  # 2
            ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']   # 1
        ]

    def print_board(self):
        """Takes no parameter. Prints the game board to output with axis labels in terms of user command coordinates
        and array indices"""
        print('    a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t')
        print('    0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19')
        i = 20
        for row in self._board:

            print(str(20 - i), end='  ')
            if i > 10:
                print(' ', end='')

            for place in row:
                print(place, end='  ')

            print(str(i))
            i -= 1
        print('    a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t')
        print('    0  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18 19')

    def get_game_state(self):
        """Takes no parameters and returns  the current game state data member of the object."""
        return self._game_state

    def get_current_player(self):
        """Takes no parameters and returns  the current player data member of the object."""
        return self._player

    def get_board(self):
        """Takes no parameters and returns the current game board"""
        return self._board

    def resign_game(self):
        """Takes no parameters and allows the current player to forfeit the current game, changing the
        game state accordingly"""
        if self._player == 'B':
            self._game_state = 'WHITE_WON'
        else:
            self._game_state = 'BLACK_WON'

    def make_move(self, start_comm, end_comm):
        """
        A method which takes a starting and ending coordinates and moves the current player's piece at those
        coordinates to the ending coordinate if the move is legal. Any pieces are captured at the destination footprint
         and True is returned. The game state is updated if this was a winning move. Returns False if the move is
         illegal or the game is already over.

        First, get_game_state is called to see if the game is still running.
        The user commands are translated to array indices [row,col] in the board by the command_to_index method.
        The method determines that the coordinates are inside the playable area, returns False otherwise.
        Then, the move vector direction and magnitude are calculated and stored as variables: delta_row, delta_col, mag
        The method creates a new Piece object at the starting coordinates and by passing the GessGame object itself.
        It then calls is_legal for that object and returns false if not legal.
         The method then deletes the original piece tokens and begins moving the piece by updating the current_position
         of the piece according to the vector, checking if the footprint encounters any other tokens after each move.
         If the piece completes its vector course without first running into
         other tokens, running off the board, or removing the current player's last king, the method finishes the move
         and returns True.(returns False otherwise) Tokens at the final footprint are deleted and the original piece
          shape is pasted to the destination using paste_here. Edges are cleared using clear_edge
          has_ring is called during the move and afterwards to
          determine 1st if the move is legal, and then to see if the legal move resulted in a win. The current player
          is then updated.
        """

        # Save the original board in case we need to revert the move
        original = []
        for i in self._board:
            original.append(list(i))
        # Check if game is already over
        if self.get_game_state() != "UNFINISHED":
            return False
        # Translate command to array indices
        start_coord = self.command_to_index(start_comm)
        end_coord = self.command_to_index(end_comm)
        # Check if center of piece is inside playable area at start and end
        if start_coord[0] <= 0 or start_coord[0] >= 19:
            return False
        elif start_coord[1] <= 0 or start_coord[1] >= 19:
            return False

        if end_coord[0] <= 0 or end_coord[0] >= 19:
            return False
        elif end_coord[1] <= 0 or end_coord[1] >= 19:
            return False
        # Calc the total change in position during the move
        change_row = end_coord[0] - start_coord[0]
        change_col = end_coord[1] - start_coord[1]

        # Validate that the vector is in one of 8 allowed directions and create unit vector variables.
        if change_row == 0 and change_col == 0:
            return False
        elif change_row != 0 and change_col != 0 and abs(change_row) != abs(change_col):
            return False
        mag = max(abs(change_col), abs(change_row))
        delta_row = int(change_row / mag)
        delta_col = int(change_col / mag)

        # Create a piece at the location and check if it is legal
        a_piece = Piece(self, start_coord)
        if not a_piece.is_legal(delta_row, delta_col, mag):
            return False

        # delete the original piece tokens from board
        for row in range(start_coord[0]-1, start_coord[0]+2):
            for col in range(start_coord[1] - 1, start_coord[1]+2):
                self._board[row][col] = '-'

        # if this move destroys the players only ring and the piece is not their last ring, revert and return False
        if not self.has_ring() and not a_piece.get_ring():
            self._board = original
            return False

        # take steps in the unit vector direction until magnitude is reached
        steps = 0
        while steps < (mag - 1):
            a_piece.move_pos(delta_row, delta_col)
            pos = a_piece.get_current_pos()
            steps += 1
            # check footprint of piece for other tokens, revert and return False if other tokens present(move is not
            # yet completed)
            for row in range(pos[0] - 1, pos[0] + 2):
                for col in range(pos[1] - 1, pos[1] + 2):
                    if self._board[row][col] != '-':
                        self._board = original
                        return False
        # move the last step
        a_piece.move_pos(delta_row, delta_col)

        # paste the shape of the piece over the current footprint
        self.paste_here(a_piece)

        # delete tokens outside play area
        self.clear_edge()
        self.change_player()
        # check if player has won
        if not self.has_ring():
            if self._player == "W":
                self._game_state = 'BLACK-WON'
            else:
                self._game_state = 'WHITE_WON'

        return True

    def change_player(self):
        """Takes in no arguments. Switches the current player to the other."""
        if self._player == 'B':
            self._player = 'W'
            return
        self._player = 'B'

    def clear_edge(self):
        """After a move, this is called to clear tokens which are outside of the play area"""
        for row in range(0,20):
            for col in range(0,20):
                if row == 0 or row == 19 or col == 0 or col == 19:
                    self._board[row][col] = '-'

    def command_to_index(self, command):
        """Takes in a user command such as 'e5' and returns the array row and column indices in the game board
        corresponding to that command as a list"""
        col = ord(command[0]) - 97

        row = 20 - int(command[1:])
        return [row, col]

    def has_ring(self):
        """Takes in nothing and checks if the current player has a ring still on the board. Returns True if a
        ring is present, False otherwise. Works by finding empty places on the board, creating a piece there and seeing
        if that piece is a ring for the current player."""

        for row in range(1, 18):
            for col in range(1, 18):
                if self._board[row][col] == '-':
                    a_piece = Piece(self, [row, col])
                    if a_piece.get_ring():
                        return True
        return False

    def paste_here(self, piece):
        """Pastes the shape of the passed piece object to the pieces current position on the game board, deleting
        any tokens that previously occupied the footprint."""
        pos = piece.get_current_pos()
        row = pos[0]
        col = pos[1]
        shape = piece.get_shape()
        # Iterate across the footprint of the piece and paste in the corresponding token at that point in the shape.
        for r_offset in range(-1,2):
            for c_offset in range(-1,2):
                self._board[row + r_offset][col + c_offset] = shape[1 + r_offset][1 + c_offset]

class Piece:
    """Represents a potential piece in a game of Gess. Tracks the starting location, current location, directional
     vector and shape of the specified piece. A Piece is created during a make_move call by the GessGame Class and
     used only once during that specific call. is_legal handles legality in the formation of the piece"""

    def __init__(self, game, start_coord):
        """Creates a 3x3 piece on the board centered at the start position in make_move. The piece may or may
        not be legal to create. The origin, current position, shape, and current player are saved as data
        members. Logic determines if the piece is a ring or not and stores this info as a data member"""

        self._origin = start_coord
        self._current_pos = start_coord
        board = game.get_board()
        row = start_coord[0]
        col = start_coord[1]

        # store tokens at each location in the footprint
        self._shape = [[board[row - 1][col - 1], board[row - 1][col],  board[row - 1][col + 1]],
                           [board[row][col - 1],     board[row][col],      board[row][col + 1]],
                           [board[row + 1][col - 1], board[row + 1][col],  board[row + 1][col + 1]]]

        self._current_player = game.get_current_player()

        # Check if the piece is a ring and mark it accordingly in self._ring
        if self._current_player == "B" and self._shape == [ ['B', 'B' , 'B'],
                                                            ['B', '-'  , 'B'],
                                                            ['B', 'B' , 'B']]:
            self._ring = True
        elif self._current_player == "W" and self._shape == [   ['W', 'W' , 'W'],
                                                                ['W', '-'  , 'W'],
                                                                ['W', 'W' , 'W']]:
            self._ring = True
        else:
            self._ring = False

    def get_origin(self):
        """Returns the origin data member of the piece object"""
        return self._origin

    def is_legal(self, delta_row, delta_col, mag):
        """Takes in unit vector values and magnitude from make_move and returns False if this piece is not legally able
        to move according to that vector or if the creation of the piece is illegal based on having other player's
        tokens in the shape. Returns True if the piece is legal"""
        # Validate that no other player tokens inside shape
        for row in self._shape:
            for place in row:
                if place != '-' and place != self._current_player:
                    return False

        # Calculate the shape index to check to allow the desired movement direction.
        check_row = 1 + delta_row
        check_col = 1 + delta_col

        # Check that token is present at indices required for chosen movement
        if self._shape[check_row][check_col] == '-':
            return False
        if mag > 3 and self._shape[1][1] == '-':
            return False
        return True

    def get_ring(self):
        """Returns the ring data member of the piece object"""
        return self._ring

    def move_pos(self,delta_row,delta_col):
        """Changes the piece's current position data member by the row and column deltas given as parameters"""
        self._current_pos[0] += delta_row
        self._current_pos[1] += delta_col

    def get_current_pos(self):
        """Takes in nothing. Returns the Piece object's current positon as [row,col]"""
        return self._current_pos

    def get_shape(self):
        """""Takes in nothing and returns the piece object's shape data member"""
        return self._shape
