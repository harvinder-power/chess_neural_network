# Tic-Tac-Toe
## Introduction
Variant of the classic game Tic-Tac-Toe to incorporate temporal difference based learning. In brief, the computer creates a lookup table which it uses to choose its next move. However, it randomly decides to explore new probabilities to determine if it provides a significant advantage in further play, with a feedback loop to reinforce this action.

## Initialisation
To use this game, the following packages have to be installed - numpy, itertools, pickle, h5py. These can be done through the following commands in terminal:

```
>> sudo easy_install pip
>> pip install numpy
>> pip install itertools
>> pip install pickle
>> pip install h5py
```
All the relevant packages should now be installed, and you should be ready to go!

The script can be run in the command line with the following command:

```
>> python TemporalDifference.py
```
Alternatively, the script can be run using Jupyter Notebook (see [Jupyter.org](http://jupyter.org) for more details on installation)

## Modification
Sections [1] to [5] in the notebook are to setup the game itself.

Section [7] contains the parameter `trainFromScratch` which is initially set to `True`. This can be modified to be `False` to shorten processing time in later runs. The parameter `trainAtAll` can also be set to `False` to not use a training algorithm altogether.

The training process iterates through the future states to find the best one in terms of the value function, V.

To allow the algorithm to learn - the following line of code is used:
```
# Explore suboptimal states with some probability
if np.random.uniform() < exploreProbability:
    #print 'Explore step'
    # Don't randomly explore if we are on the verge of a win
    if abs(maxValue - 1.0) < 1e-12:
        newState = futureStates[maxIdx]
        V[curState] = V[curState] + stepSize * (V[newState] - V[curState]) 
        #print V[curState]
        curState = newState
```
The parameter `exploreProbability` can be modified to search for better outcome at a higher, or lower rate. The default is set to 0.4.

Running the code in section [7] generates pickles the valuetable to a file called `valuetable.txt`. If this has already been generated, it can be read rather than re-generating the file (change `trainFromScratch` from True to False).

## Playing against the computer
Running section [10] will then run the game and allow you to play tic-tac-toe in terminal against the computer.

All future states are printed with the value function of each move printed below to detemine which move has the highest chance of success.

