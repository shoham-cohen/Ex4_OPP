# Ex4_OPP
![pokemon-pokemon-first-generation-wallpaper-preview](https://user-images.githubusercontent.com/93212774/148692702-00cc8da3-87f4-4b17-a08a-a7bd4d035cbc.png)


* Written by Shoham Cohen and Yehonatan Baruchson.
## position
Object that stores 3 values:
* double x
* double y
* double z
The constructor recives a String and splits him to the 3 values.

## EdgeData
EdgeData is an object that stores 3 values:
* int src
* int des
* double w

### Methods
* getSrc: return the id of the source NodeData of the edge.
* getDes: return the id of the destination NodeData of the edge.
* getWeight: return the weight of the edge.

## NodeData

Nodedata is an object that stores 3 values:
* nodedata ID.
* nodedata position.
* nodedata Dict of all the edges that related to this node.

### Methods
* GetKey: returns the ID of the Node
* GetLocation: returns the positon of the Node
* SetLocation: changes the position of thr Node to the inputted position

## DiGraph

DiGraph is an object that stores 3 values:
* Dict of NodeDatas.
* int NumOfEdges: number of the edges in the graph.
* int MC: parameter that helps us to track changes in the graph.

### Methods
* v_size: returns the number of nodes on the graph.
* e_size: returns the number of Edges in the graph.
* get_all_v: returns a Dict with all the nodes in the graph.
* all_in_edges_of_node: return a Dict of all the nodes who has an edge that her dest is the inputted node.
* all_out_edges_of_node: return a Dict of all the nodes who has an edge that her source is the inputted node.
* get_mc: returns the MC.
* add_edge: addind the inputted edge, returns True if added succesfully.
* add_node: addind the inputted node, returns True if added succesfully.
* remove_node: delete the Node and all of his Edges from the graph, returns True if added succesfully.
* remove_edge: delete the specific inputted Edge, returns True if added succesfully.

## Agent

Agent is an object that stores 9 values:
* id of the Agent
* value of the Agent
* speed of the Agent
* time to get to pokemon
* src 
* dest
* Next pokemon to catch
* pos of the Agent
* preference  

## Pokemon

Pokemon is an object that stores 6 values:
* value of the Pokemon
* src of the edge that the Pokemon is on
* dest of the edge that the Pokemon is on
* pos of the Pokemon
* Agent that is going to catch the Pokemon
* Type of the pokemon  

## TheGame
Object that stores 3 values:
* AgentsList list of the Agents in the game
* graph is the DiGraph of the game
* PokeList list of the Pokemons in the game

### Methods
* setNewVal - updating the game values
* findPokeEdge- find on which edge every pokemon standing
* allocateAgent - allocate pokemon to agent
* sleep - keeping that the amount of moves wont pass the allowed amount
* shortest_path - finds the shortest path between two nodes
* dikjestra - dikjestra algorithem

## RESULTS
<img width="160" alt="res" src="https://user-images.githubusercontent.com/93212774/148694740-a838f9bd-bb1a-4afb-83c7-ce79b2f98494.png">


## HOW TO RUN
* run the server using the command java -jar Ex4_Server_v0.0.jar 11 then run the Ex4.py file, enjoy :)

![screen-capture](https://user-images.githubusercontent.com/93212774/148693505-86528dd5-cc17-4166-8d2d-61b1396d4cab.gif)

