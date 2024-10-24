# Example usage
m_dfs = Maze('maze1.txt')
m_dfs.solve(algorithm='DFS')
print("DFS States Explored:", m_dfs.num_explored)

m_bfs = Maze('maze1.txt')
m_bfs.solve(algorithm='BFS')
print("BFS States Explored:", m_bfs.num_explored)