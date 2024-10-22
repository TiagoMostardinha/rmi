#!/bin/bash
EXERCISE="C1"

# MAP configuration
ARGS=" --param ../Labs/rmi-2425/C1-config.xml"
ARGS+=" --lab ../Labs/rmi-2425/C1-lab.xml"
ARGS+=" --grid ../Labs/rmi-2425/C1-grid.xml"
ARGS+=" --scoring 1"

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
tmux split-window -v -t $EXERCISE


tmux send-keys -t $EXERCISE:1.2 'cd ./labyrinth/simulator; ./simulator --param ../Labs/rmi-2425/C1-config.xml --lab ../Labs/rmi-2425/C1-lab.xml --grid ../Labs/rmi-2425/C1-grid.xml --scoring 1' C-m
sleep 2
tmux send-keys -t $EXERCISE:1.3 'cd ./labyrinth/Viewer; ./Viewer --autoconnect' C-m
sleep 1
tmux send-keys -t $EXERCISE:1.1 'cd ./client/'$EXERCISE'; python3 main.py' C-m

tmux attach-session -t $EXERCISE
