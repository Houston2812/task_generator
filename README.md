# Task generator
This is a message queue based on ØMQ.   
The system receives a .cvs file and analyzes it. This process has the following structure:
1. __Task generator__ reads the file provided by the user and sends to the __data separator__.
1. __Data separator__ separates the data into small pieces and sends to the __analyzers__.
1. __Analyzers__ convert __date of birth__ to the __age__ and send to the __reducer__.
1. __Reducer__ receives data from all analyzers and collects it into array of tuples that later get sorted by the _age_. The sorted data is sent back to the __task generator__.


In order to function properly files should be run in the following order:
1. python3 reducer.py
1. python3 analyzer.py - if you want to have a lot of analyzers run this program multiple times in different terminals.
1. python3 data_separator.py
1. python3 task_generator.py - when running this program it will ask user for the name of file that should be processsed. 
