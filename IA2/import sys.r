import sys

# Create a table to compare results
table = """
<table>
  <tr>
    <th>Labyrinth</th>
    <th>Algorithm</th>
    <th>States Explored</th>
    <th>Solution Found</th>
  </tr>
"""

# Run DFS and BFS for each labyrinth
for labyrinth in ["maze1.txt", "maze2.txt"]:
    m = Maze(labyrinth)
    print("Maze:", labyrinth)
    m.print()
    print("Solving with DFS...")
    m.solve("DFS")
    print("States Explored:", m.num_explored)
    print("Solution:")
    m.print()
    table += f"""
  <tr>
    <td>{labyrinth}</td>
    <td>DFS</td>
    <td>{m.num_explored}</td>
    <td>{m.solution is not None}</td>
  </tr>
"""

    m = Maze(labyrinth)
    print("Solving with BFS...")
    m.solve("BFS")
    print("States Explored:", m.num_explored)
    print("Solution:")
    m.print()
    table += f"""
  <tr>
    <td>{labyrinth}</td>
    <td>BFS</td>
    <td>{m.num_explored}</td>
    <td>{m.solution is not None}</td>
  </tr>
"""

table += "</table>"

# Write the table to an HTML file
with open("index.html", "w") as f:
    f.write(table)