# Tic-Tac-Toe

## Introduction
Variant of the classic game Tic-Tac-Toe to incorporate Temporal Difference Reinforcement Learning. In brief, the computer creates a lookup table which it uses to choose its next move. However, it randomly decides to explore new states to avoid falling into the trap of only visiting familiar states. We hope to prevent our Tic Tac Toe bot from experiencing blissful ignorance when navigating the state space!

## Literature
This code is based upon the Tic Tac Toe example from Chapter 1 of [_Reinforcement Learning: An Introduction_](http://people.inf.elte.hu/lorincz/Files/RL_2006/SuttonBook.pdf) by Sutton and Barto.

The learning equation powering this code is the Temporal Difference update equation:

$V(s) = V(s) + \alpha [V(s') - V(s)]$

## Platforms
Our code thus far has only been tested on Mac OSX. It is safe to assume it will also work on Linux and Windows but if you have problems on other platforms, please raise an issue or submit a Pull Request if you know the fix!

## Initialisation
To use this game, the following packages have to be installed - numpy, itertools, pickle, h5py. This can be achieved by running the following commands in terminal:

```
>> sudo easy_install pip
>> pip install numpy
>> pip install itertools
>> pip install pickle
>> pip install h5py
```
All the relevant packages should now be installed, and you should be ready to go!

The script can be run in a terminal with the following command:

```
>> python main.py
```

To train a new model from scratch, simply delete the _valuetable.txt_ file. This file stores a pretrained model that works well in our experience. 

## Modification

In _main.py_ changing the _n_episodes_ parameter will affect the performance of the trained model. Too few episodes will lead to a poor Tic Tac Toe player, and too many episodes will lead to a long training time. In our experience, 100000 episodes is the 'sweet spot'.

The computer plays as 'X' by default, but can be changed to play as 'O' by setting _player_idx_ to 2 when initialising the ReinforcementEngine. The _learning_rate_ can also be changed. A small learning rate avoids falling into local minima, but decreases the convergence rate. A large learning rate may converge faster by may also 'overshoot' the minimum and lead to poor results. We recommend setting the _learning_rate_ to 0.01. As mentioned earlier, _explore_probability_ is used to prevent the learning agent from only exploring previously visited areas of the state space. Increasing this probability will improve the chances that the agent will explore the entire search space. However, when performing exploration steps, the temporal difference update isn't performed. As such, too much exploration will lead to not enough learning. We find that setting _explore_probability_ to 0.4 works well (i.e. 'explore random states 40% of the time').

## Playing against the computer
Running section [10] will then run the game and allow you to play tic-tac-toe in terminal against the computer.

All future states are printed with the value function of each move printed below to detemine which move has the highest chance of success.

