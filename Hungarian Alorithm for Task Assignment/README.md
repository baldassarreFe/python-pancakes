# Hungarian Algorithm for Task Assignment
## Definition of the problem
Suppose to have a city modeled as a graph. Starting from its adjacency matrix it is possible to build another matrix holding the shortest path between every pair of nodes in the graph.

Now, in the city there are ambulances, patients and hospitals. The goal of the ambulances is to pick a patient and bring him to the nearest hospital. If there are more ambulances than patients the goal of the vehicle will be to reach a node that is optimal for covering the area.

We have to assign every ambulance to a task in such a way that the sum of all the travel costs is minimum. The cost of a task depends on the task:
* **saving a patient:** total cost  = travel to the patient + travel to the nearest hospital
* **reaching a node** total cost = travel to that node

Using the shortest paths matrix it is possible to build another matrix representing all the costs that come from the association of an ambulance to a task. This matrix will have as many rows as the number of ambulances and a number of columns equal to ```max(patients, patients + (ambulances - patients))```. The second value comes from assigning one ambulance to every patient and sending the remaining ones to some node.

|           |**Save Pat 1**|**Save Pat 2**|**Reach Node F**|**Reach Node T**|
|-----------|:------------:|:------------:|:--------------:|:--------------:|
| **Amb 1** |    12 + 4    |     4 + 5    |       12       |       4        |
| **Amb 2** |    5 + 3     |     9 + 1    |       21       |       27       |
| **Amb 3** |    4 + 2     |     2 + 4    |       10       |       8        |
| **Amb 4** |    2 + 1     |    12 + 7    |       10       |       15       |

|           |**Save Pat 1**|**Save Pat 2**|**Save Pat 3**|
|-----------|:------------:|:------------:|:------------:|
| **Amb 1** |    12 + 4    |     4 + 5    |    9 + 12    |
| **Amb 2** |    5 + 3     |     9 + 1    |    4 + 19    |

Given this set up it is possible to use the Hungarian Algorithm<sup id="a1">[1](#f1)</sup><sup id="a2">,[2](#f2)</sup> to assign every ambulance to a task minimizing the distance traveled.

## Dealing with priorities
To account for the severity of the accidents it is possible to weight the travel distances dividing by a value representing the patient's priority to be saved.

|           |**Save Pat 1 [3]**|**Save Pat 2 [2]**|**Save Pat 3 [5]**|
|-----------|:----------------:|:----------------:|:----------------:|
| **Amb 1** |    (12 + 4)/3    |     (4 + 5)/2    |    (9 + 12)/5    |
| **Amb 2** |    (5 + 3)/3     |     (9 + 1)/2    |    (4 + 19)/5    |

In such a way the algorithm will favor the patients with higher priority.

#### Credits
The code that solves the Hungarian problem belongs to [this repo](#https://github.com/tdedecko/hungarian-algorithm) and is released under MIT licence.

1. <a id="f1">Formally on [Wikipedia](#https://en.wikipedia.org/wiki/Hungarian_algorithm)</a> [↩](#a1)
2. <a id="f2">Step by step on  [WikiHow](#http://www.wikihow.com/Use-the-Hungarian-Algorithm)</a> [↩](#a2)
