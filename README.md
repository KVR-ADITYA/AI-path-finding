# AI-Path Finding

## Description : This project is the implementation of AI search algorithms to solve mages

![image](./images/maze.PNG)

## How to run?
<pre>
	<code> pip install reqirements.txt </code>
	<code> python main.py</code>
</pre>

<p>In this project we have implemented two algorithms(A* and DFS).Feel free to implement and add more
algorithms you know.If you want to add your own fun mazes to the project write your own txt file in the format of maze.txt
Note that the window size is onl 255x255</p>

<p>
If you want to make a custom maze and use the algorithm to solve it then you can do it in the following steps.
First create a file in the ./input path.(It should be a txt file)
Then use the following convention to create the maze:
<pre>
<code>X -> start point</code>
<code>Y -> end point</code>
<code>O -> blocking point</code>
<code>. -> free point</code>
</pre>

For example, the above maze should look like:
<pre>
<code>..........</code>
<code>......O...</code>
<code>..O.......</code>
<code>.....O....</code>
<code>..........</code>
<code>O.........</code>
<code>....XO....</code>
<code>.Y.......O</code>
<code>.O........</code>
<code>...O......</code>
</pre>
</p>

