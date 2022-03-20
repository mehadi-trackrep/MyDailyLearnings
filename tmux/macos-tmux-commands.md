*** At first, we have to run the tmux session where the command is - `tmux`

### Some ==terminologies==:-
```
    ** Prefix
    ** Session
    ** Window
    ** Pane
```

    - create new session
    - attach a session
    - detach from a session


### The tmux `prefix` is `ctrl + b`

*** Before anything do command, we have to use the 'prefix' command at first and then
without holding key again press the new keys/commands:-

* `tmux ls` ==> [for getting total existed and running tmux sessions]
* `tmux new -s mehadi`  ==> [to generate a new session named mehadi]
* `tmux attach-session -t mehadi`   ==> [to attach with already existing session named mehadi for example in here]
* `prefix` + `c` ==> [for creating a new window]
* `prefix + 0/1/2..` ==> [to switch from each bash pane to another pane]
* `prefix + d`  ==> [to detach from the running session without hampering!]

** `htop` ==> [to know about the CPU and memory usage]


#### `Reference:` 
* https://linuxize.com/post/getting-started-with-tmux/
* https://jeongwhanchoi.medium.com/install-tmux-on-osx-and-basics-commands-for-beginners-be22520fd95e