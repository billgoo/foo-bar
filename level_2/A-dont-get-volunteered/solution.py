
class Node:
    def __init__(self, num, dis):
        self.pos = num
        self.dis = dis


class Board:
    def __init__(self, size,
        movements=[(1, 2), (1, -2), (-1, 2), (-1, -2),
                   (2, 1), (2, -1), (-2, 1), (-2, -1)]):
        self.size = size
        self.MOVEMENTS = movements

    def node_axis(self, num):
        """
        x, y of node
        """
        return int(num // self.size), int(num % self.size)

    def node_num(self, x, y):
        """
        x, y of node
        """
        return int(x * self.size + y)

    def valid(self, x, y):
        """
        if node is on the board
        """
        return True if 0 <= x < self.size and 0 <= y < self.size else False

    def bfs_distance(self, start, end):
        """
        shortest distance by bfs
        """
        queue = []
        queue.append(start)
        visited = {}

        while queue:
            # first node in queue
            node = queue.pop(0)

            # return when destination is reached
            if node.pos == end.pos:
                return node.dis

            # process nodes that have not been visited
            if node.pos not in visited:
                # mark node as visited
                visited[node.pos] = True

                # validate piece movement
                for (x_, y_) in self.MOVEMENTS:
                    x, y = self.node_axis(node.pos)
                    x, y = x + x_, y + y_

                    # queue valid moves only
                    if self.valid(x, y):
                        queue.append(Node(self.node_num(x, y), node.dis + 1))

        return float('inf')


def solution(src, dest):
    #Your code here
    start, end = Node(src, 0), Node(dest, 1000000000)
    board = Board(8)
    return board.bfs_distance(start, end)
