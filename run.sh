#!/bin/bash
EXERCISE="C1"
CLIENT_PROGRAM="main.py"

source ./venv/bin/activate

# delete previous session of $EXERCISE
tmux has-session -t $EXERCISE 2>/dev/null
if [ $? == 0 ]; then
  tmux kill-session -t $EXERCISE
fi

sleep 0.1

# create a new session
tmux new-session -d -s $EXERCISE

# split the window
tmux split-window -h -t $EXERCISE

# run the command in the first pane
tmux send-keys -t $EXERCISE:1.1 'cd ./labyrinth/ && ./start'$EXERCISE'' C-m

sleep 2

tmux send-keys -t $EXERCISE:1.2 'cd ./client/'$EXERCISE' && python3 '$CLIENT_PROGRAM'' C-m

# attach to the session
tmux attach-session -t $EXERCISE
