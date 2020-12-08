# Night-School

My data structures and algorithms notes. This is probably a precursor to a bigger more ambitious project... 

### Data Structures

The goal here is to create a complete list of existing, documented data structures, and map them to:
* a table of best average worst case operation runtimes, complete with list of invariants for each case.
* a list of algorithms available to that data structure

Additionally, we would like to figure out, where possible, the time and memory requirements for transforming data from one structure to another structure, and provide a mechanism
for determining whether for some operation, there is a performance benefit to be gained by converting the data to another data structure and performing the intended operation using some algorithm available to the new data structure.

### Algorithms

The goal here is to create as complete a list of algorithms as is possible with:
* The input data type or structure
* The output data type or structure
* A limited set of output descriptors (i.e. true/false/minimum/maximum, value/set)
* A table best / average / worst case runtime complexity complete with invariants for each case (e.g. bucket sort in O(n) if initialized with n buckets)
* The time and memory requirements
* Categorical classifications
* Source for solid python implementations from industry standard libraries or builtins if they exist (i.e. `networkx` for graphs, `heapq` for heaps) or write them if they do not exist, (or if they seem like they would be interesting or fun to implement)
* Eventually, source for implmentations in C, C++, C#, Go, Java, JS, Ruby

### Utils

Here we will keep utility functions for common operations. Any time we have to write code to perform some 'relatively' atomic action, we will stash it here.

`files.py`

Thin wrappers for in-program file operations
* read
	* all
	* lines
	* n-bytes
* write
* copy
* move
* delete
* read_permissions
* change_permissions
* stat/metadata


`system.py`

Calls to get info about system
* cpu
* memory
* PCI bus
* USB
	* Read from serial device
* devices
* network
* firmware
* OS
	* version
	* file system
* processes
* libraries
	* files
	* dependencies


`regex.py`

A list of regex patterns that can be imported
* common patterns


`pipes.py`

* Calling external programs
* threading patterns
* sockets
* OS-level IPC
* Multiple launch pattern to bypass GIL


`concurrency.py`

* threads
* asyncio
* defeating GIL


`network.py`

* web requests
* raw http requests
* web sockets


`database.py`

* common interaction patterns
	* Raw SQL Queries
	* Postgres
	* MySQL
	* Elasticsearch
	* MongoDB


### The Glossary

'''glossary.py''' is a little system to navigate through note files in the source. The goal is to be able to navigate through the project structure and read notes in a TUI from the CLI.

I'm using Markdown here because I want to read the documentation, but you might want to use YAML if you want to run the documentation ;)

The idea behind the glossary system is in repo documentation. (because when was the last time it was super-convenient and conducive to the true object of your feeble modern attention span to leave your editor/IDE, open a browser, login to web service, navigate to the appropriate documentation, read through it until you find what your looking for, switch back, and act on that information, I tell you what.. I can't remember the last time it was for me)

I just thought it sounded like something practical to have fleshed out and well developed for real projects, and that this would be a good place to experiment with the implementation without pressure or consequences.

Note files are denoted as '''entry.gls''' This might be a terrible idea. I can see a few ways that this becomes cumbersome, and 

Once this is a little more developed it should be broken out into it's own repo, and made installable.
