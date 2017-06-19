import pickle
import itertools
import numpy as np
import os
from game import Game

# Uses Temporal Difference learning to play Tic Tac Toe
class ReinforcementEngine:

    # Initialise the engine to play as either
    # 'X' = player_idx 1, or 'O' = player_idx 2
    def __init__(self, player_idx=1, learning_rate=0.01, explore_probability=0.4):
        self.player_idx = player_idx
        self.learning_rate = learning_rate
        self.explore_probability = explore_probability
        
        if player_idx == 1:
            self.opponent_idx = 2
        else:
            self.opponent_idx = 1
            
        self.is_v_initialised = False
        self.V = {}
    
    
    # Initialises V table.
    # - Winning states are initialised to 1
    # - Losing and drawn states are initialised to 0
    # - Non-terminal states are initialised to 0.5
    def init_v(self):
        self.is_v_initialised = True
        for combination in itertools.product(xrange(3), repeat=9):
            game = Game()
            game.board = list(combination)
            if game.is_won() == self.player_idx:
                self.V[combination] = 1.0
            elif game.is_drawn() or game.is_won() == self.opponent_idx:
                self.V[combination] = 0.0
            else:
                self.V[combination] = 0.5
               
            
    # Loads V table from filename
    def init_v_from_file(self, filename):
        if os.path.exists(filename):
            print 'Loading pretrained file...'
            with open(filename, 'rb') as handle:
                self.V = pickle.loads(handle.read())
               
            
    # Saves V table to filename         
    def save_v_table_to_file(self, filename):
        with open(filename, 'wb') as handle:
            pickle.dump(self.V, handle)
        
        
    # Performs Temporal Difference update: 
    # V(s_cur) = V(s_cur) + alpha
    # -----------------------------------------------------
    # s_cur and s_next are tuples describing 2 board states
    def perform_td_update(self, s_cur, s_next):
        if not self.is_v_initialised:
            print 'V table is not initialised! Please call init_v() first.'
        if len(self.V) == 0:
            print 'V table is empty. Cannot perform TD update!'
            
        self.V[s_cur] = self.V[s_cur] + \
                        self.learning_rate * (self.V[s_next] - self.V[s_cur])
    
    # Trains V table by playing engine against itself
    def train(self, n_episodes=100000):
        for i in xrange(n_episodes):
            game = Game()
            while True:
                # -------------------- Make Move --------------------------
                next_state = self.get_best_future_state(game)

                # Check if we are on the verge of a win
                tmp_game = Game()
                tmp_game.board = list(next_state)
                finish_now = False
                if tmp_game.is_won() == self.player_idx:
                    finish_now = True

                if np.random.uniform() > self.explore_probability or finish_now: 
                    self.perform_td_update(tuple(game.board), next_state)
                    game.board = list(next_state)    
                else:
                    # Select a random state to explore
                    next_state = self.get_random_future_state(game, self.player_idx)
                    game.board = list(next_state)

                if game.is_won() == self.player_idx or game.is_drawn():
                    break
                # ---------------------------------------------------------

                # ---------------- Make Adversary Move --------------------
                next_state = self.get_worst_future_state(game)

                # Check if we are on the verge of a win
                tmp_game.board = list(next_state)
                finish_now = False
                if tmp_game.is_won() == self.opponent_idx:
                    finish_now = True

                if np.random.uniform() > self.explore_probability or finish_now:
                    self.perform_td_update(tuple(game.board), next_state)
                    game.board = list(next_state)

                else:
                    # Select a random state to explore
                    next_state = self.get_random_future_state(game, self.opponent_idx)
                    game.board = list(next_state)

                if game.is_won() == self.opponent_idx or game.is_drawn():
                    break
                # ---------------------------------------------------------
            
    # Used when playing against a human opponent
    def get_best_move_idx(self, game):
        next_state = self.get_best_future_state(game)
        for i in xrange(len(next_state)):
            if next_state[i] != game.board[i]:
                return i
            
        # Should only reach here if the logic is seriously flawed...
        return -1
                
    # Utility Function.
    # Returns a random state from the possible
    # future states.
    def get_random_future_state(self, game, player_idx):
        next_states = game.get_next_states(player_idx)
        n_next_states = len(next_states)
        random_state_idx = int(n_next_states * np.random.uniform())
        return next_states[random_state_idx]
    
    # Utility Function.
    # Returns the best future state
    def get_best_future_state(self, game):
        next_states = game.get_next_states(self.player_idx)
        n_next_states = len(next_states)
        if n_next_states == 0:
            print 'No future states available!'
            return ()
        
        max_idx = 0
        max_value = self.V[next_states[max_idx]]
        for i in xrange(n_next_states):
            if self.V[next_states[i]] > max_value:
                max_value = self.V[next_states[i]]
                max_idx = i
                
        return next_states[max_idx]
    
    # Utility Function.
    # Returns the worst future state.
    # Used for simulating an adversary.
    def get_worst_future_state(self, game):
        next_states = game.get_next_states(self.opponent_idx)
        n_next_states = len(next_states)
        if n_next_states == 0:
            print 'No future states available!'
            return ()
        
        min_idx = 0
        min_value = self.V[next_states[min_idx]]
        for i in xrange(n_next_states):
            if self.V[next_states[i]] < min_value:
                min_value = self.V[next_states[i]]
                min_idx = i
                
        return next_states[min_idx]
