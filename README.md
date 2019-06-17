# Searching Algorithms

<img src="https://img.shields.io/badge/license-MIT-green.svg" />  <img src="https://img.shields.io/badge/version-1.0-red.svg" /> 

This project includes some searching algorithms to get the shortest route between two Romanian Cities.

***

## Romania Map

This map includes costs between its cities:

<img src="./Romania Map.png"/>

## Tested Algorithms

1. **BFS (Breadth First Search)**: This algorithm inserts cities in Data Structure (Queue) using a *FIFO* procedure.
2. **DFS (Depth First Search)**: This algorithm inserts cities in Data Structure (Stack) using a *LIFO* procedure.
3. **Branch and Bound**: This algorithm inserts cities in Data Structure ordering them using their *path_cost*.
4. **Branch and Bound with Heuristic**: This algorithm inserts cities in Data Structure ordering them using their *path_cost + underestimated heuristic (distance in straight line to Destination City from Node City)*

## Files

- You can see some **Tests & Output Results** commented in *run.py* file.
- You can see **Main Algorithm** in *search.py* file.
- You can see **Stacks Implementations** in *utils.py*

## How to Run Project:

This project has been tested using *Python 3*. If you want to run it, execute in console in Repository Directory:

```bash
python3 ./run.py
```

## Output

You are able to try some new Tests. Just modify the cities in *run.py* changing parameters in *search.GPSProblem(city1, city2, search.romania)* method!

Output should be something like this:

```bash
======================================[CASO_1]  <= Example Number
Nodos visitados:  16                            <= Visited Nodes [BFS]
En Anchura: [<Node B>, <Node F>, <Node S>, <Node A>]  <= Trace [BFS]
Nodos visitados:  10                            <= Visited Nodes [DFS]
En Profundidad: [<Node B>, <Node P>, <Node C>, <Node D>, <Node M>, <Node L>, <Node T>, <Node A>]  <= Trace [DFS]
Nodos visitados:  24                            <= Visited Nodes [B&B]
Branch & Bound: [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>]  <= Trace [B&B]
Nodos visitados:  6                             <= Visited Nodes [B&B w/ Heur.]
Branch & Bound con Subestimacion: [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>]  <= Trace [B&B w/ Heur.]
====================================================================================
```



## Search Stats

- **BFS and DFS** don't have to get optimal solutions, meanwhile **Branch and Bound** does.
- **B&B with Heuristic** visits less nodes than the other algorithms. Then, its computational cost is the lowest of these algorithms thanks to its heuristic.

| From 'Arad' to 'Bucharest' | Visited Nodes | Total Cost | Optimal? |
| :------------------------- | :-----------: | :--------: | :------: |
| *BFS*                      |      16       |    450     |    No    |
| *DFS*                      |      10       |    733     |    No    |
| *B&B*                      |      24       |  **418**   | **Yes**  |
| *B&B with Heuristic*       |     **6**     |  **418**   | **Yes**  |

