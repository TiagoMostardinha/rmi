#!/bin/bash
EXERCISE="startC1"
MAIN_PROGRAM="test.py"

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
tmux send-keys -t $EXERCISE:0.0 'cd ./labyrinth/ && ./'$EXERCISE'' C-m

sleep 2

tmux send-keys -t $EXERCISE:0.1 'cd ./client/ && python3 '$MAIN_PROGRAM'' C-m

# attach to the session
tmux attach-session -t $EXERCISE
