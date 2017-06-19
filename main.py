import os
from game import Game
from reinforcement_engine import ReinforcementEngine

engine = ReinforcementEngine()

pretrained_filename = 'valuetable.txt'
# Don't re-train if we already have a training file.
# Simply delete this file to force re-training.
if os.path.exists(pretrained_filename):
    engine.init_v_from_file(pretrained_filename)
else:
    engine.init_v()
    engine.train()
    engine.save_v_table_to_file(pretrained_filename);

# Play against the computer
game = Game()
while True:
    # ------------------ Computer's Turn --------------------
    engine_move = engine.get_best_move_idx(game)
    game.make_move(engine_move, engine.player_idx)
    
    game.print_board_state()
    
    if game.is_won() == engine.player_idx:
        print 'Game over. Bot wins!'
        break
        
    if game.is_drawn():
        print 'Game over. Drawn!'
        break
    # -------------------------------------------------------

    # -------------------- User's Turn ----------------------
    user_move = int(raw_input('Please enter your move: '))
    game.make_move(user_move, engine.opponent_idx)
    
    if game.is_won() == engine.opponent_idx:
        print 'Game over. You win!'
        break
        
    if game.is_drawn():
        print 'Game over. Drawn!'
        break
    # -------------------------------------------------------
