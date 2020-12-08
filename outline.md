Course Work

`utils/`

The practical mud and boots engineering part of this.

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

`concurency.py`

`network.py`

* web requests
* raw http requests
* web sockets


`database.py`

* common interaction patterns
	* Postgres
	* MySQL
	* Elasticsearch
	* MongoDB
	* GraphQL
	* One of the time series DB's if it ever comes up in my real life


`types.py`

Type Coersion Matrix
* bytes -> type
* string -> type
* int -> type
* float -> type
* fractions -> type
* hex -> type
* base64 -> type
* array -> []
* hash_table -> []

etc...


System:
Processor:
Memory:
Devices:
Network:
Firmware:

### Data Structures

The goal here is to create a complete list of existing, documented data structures, and map them to:
* a table of best average worst case operation runtimes, complete with list of invariants for each case.
* a list of algorithms available to that data structure

Additionally, we would like to figure out, where possible, the time and memory requirements for transforming data from one structure to another structure, and provide a mechanism
for determining whether for some operation, there is a performance benefit to be gained by converting the data to another data structure and performing the intended operation using some algorithm available to the new data structure.


### Algorithms

The goal is to create a list of algorithms

* Search
* Sort
	* insertion sort
	* merge sort
	* quick sort
	* bubble sort
* Graph

Depth-First search:

Breadth-First search:

Dijkstra
Dijkstra-Scholten
- Network Analysis:
- Link Analysis:
	Girvan-Newman (detect communities)

Pattern
Geometric
Mathematical:
Limit

Randomized
* Monte Carlo method
* Las Vegas method
* Noises
	* Perlin Noise


Greedy
Divide & Conquer
Backtracking
Branch & Bound
FFT:



