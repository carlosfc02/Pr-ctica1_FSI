# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

ou = search.GPSProblem('O', 'U', search.romania)

tp = search.GPSProblem('T', 'P', search.romania)

ln = search.GPSProblem('L', 'N', search.romania)

"""
print(search.breadth_first_graph_search(ab).path())
print(search.depth_first_graph_search(ab).path())
"""

print("Branch and Bound without heuristic A-B")
print(search.branch_and_bound_graph_search(ab).path())
print("\n")


print("Branch and Bound with heuristic A-B")
print(search.branch_and_bound_subestimate_graph_search(ab).path())
print("\n")


print("Branch and Bound without heuristic O-U")
print(search.branch_and_bound_graph_search(ou).path())
print("\n")

print("Branch and Bound with heuristic O-U")
print(search.branch_and_bound_subestimate_graph_search(ou).path())
print("\n")

print("Branch and Bound without heuristic T-P")
print(search.branch_and_bound_graph_search(tp).path())
print("\n")

print("Branch and Bound with heuristic T-P")
print(search.branch_and_bound_subestimate_graph_search(tp).path())
print("\n")


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
