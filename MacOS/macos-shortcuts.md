## MacOS related commands:-

* command + control(ctrl) + F  ==> [Resize window]
* control + command + Q  ==> [Screen lock]
* command + Q  ==> [Full quit a window]
* command + space  ==> [Spotlight search globally]
* command + shift + 4 ==> [Screen Shot by selecting an area]
* command + control + F ==> [Full screen / resize screen for a window]


## Homebrew related commands:-

*  brew services list
*  brew services restart mysql
*  mysql -u root -p goava ==> [We are using database - goava, password: m7157p49]
*  mysql -u root -p mysql ==> [Here the DB name is mysql, same password ]



## Development related commands:-

* source  /Users/goava/GOAVA/REPOSITORIES/GLOBAL_VENV/bin/activate.fish  ==> [I have a global python virtual environment, if we activate it in Fish shell]
* deactivate
* . .environment_variables.sh  ==> [To export the environment_variables. Don't use bash, instead have to use period(.) space( )]
* command + control + up arrow  ==> [To increase the VS code terminal window]
* command + control + down arrow  ==> [To decrease the VS code terminal window]
* ssh -fN tunnel  ==> [To create the local port-forwarding for the tunnel host]
*** I'm using 3307 for data-bio instance & 3308 for Goava-db-cluster
* lsof -i :port  ==> [To check if any process is listening on that port, i mean whether the port is free or not]
    --> For example:-
 - lsof -i :3306
 - lsof -i :3308
 - lsof -i :3309
* kill $(lsof -t -i:port)  ==> [To terminate/quit/kill any process that is listening on that port]
* kill -9 $(lsof -t -i:port)  ==> [Same task but forcefully/more violently]
* 



