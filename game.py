# Generic Tic Tac Toe class
class Game:

    def __init__(self):
        self.init_board()
        
    def init_board(self):
        self.board = [0,0,0,0,0,0,0,0,0]
    
    # Makes a move in the game.
    # moveIdx - the board index in which to make the move (0-8)
    # playerIdx - the player making the move, can be 1 or 2
    # Returns True if move was successfully made, False otherwise
    def make_move(self, moveIdx, playerIdx):
        if playerIdx != 1 and playerIdx != 2:
            print 'Invalid playerIdx. Move could not be made!'
            return False
        
        if moveIdx < 0 or moveIdx > 8:
            print 'Invalid moveIdx. Must be [0-8]'
            return False
            
        if self.board[moveIdx] != 0:
            print 'Invalid moveIdx. ' + \
                        'Board at position ' + str(moveIdx) + \
                        ' is already occupied!'
                    
        self.board[moveIdx] = playerIdx
        
    # Checks if the current board state is a draw
    def is_drawn(self):
        if self.is_won() != 0:
            return False
        
        for i in xrange(9):
            if self.board[i] == 0:
                return False
            
        return True
        
    
    # Checks if current board state is a win.
    # Returns 1 if player 1 has won, 2 if player 2 has won
    def is_won(self):
        # Check horizontal wins
        idx1 = 0
        idx2 = 1
        idx3 = 2
        for i in xrange(3):
            if self.identical_at_indices(idx1, idx2, idx3):
                return self.board[idx1]
            
            idx1 = idx1 + 3
            idx2 = idx2 + 3
            idx3 = idx3 + 3
        
        # Check vertical wins
        idx1 = 0
        idx2 = 3
        idx3 = 6
        for i in xrange(3):
            if self.identical_at_indices(idx1, idx2, idx3):
                return self.board[idx1]
            
            idx1 = idx1 + 1
            idx2 = idx2 + 1
            idx3 = idx3 + 1
            
        # Check diagonal win
        if self.board[0] == self.board[4] == self.board[8]:
            return self.board[0]
        
        # Check diagonal win
        if self.board[3] == self.board[4] == self.board[6]:
            return self.board[3]
        
        return 0
        
    
    # Print the state of the board in human-readable format
    def print_board_state(self):
        idx = 0
        lookup = {0: ' ', 1: 'X', 2: 'O'}
        bar = ' -----------------------------------------------'
        print bar
        for i in xrange(3):
            c0 = lookup[self.board[idx]]
            c1 = lookup[self.board[idx+1]]
            c2 = lookup[self.board[idx+2]]
            if c0 == ' ':
                c0 = str(idx)
            if c1 == ' ':
                c1 = str(idx + 1)
            if c2 == ' ':
                c2 = str(idx + 2)
            print '|\t' + c0 + '\t|\t' + c1 + '\t|\t' + c2 + '\t|'
            idx = idx + 3
            print bar
    
    # Returns array of next board states, given that it is 
    # playerIdx's move
    def get_next_states(self, playerIdx):
        nextStates = []
        for i in xrange(9):
            if self.board[i] == 0:
                newState = list(self.board)
                newState[i] = playerIdx
                nextStates.append(tuple(newState))
                
        return nextStates

    # Utility function. Checks if board elements at the given indices
    # are identical.
    def identical_at_indices(self, idx1, idx2, idx3):
        if self.board[idx1] == self.board[idx2] == self.board[idx3]:
            return True
        else:
            return False
