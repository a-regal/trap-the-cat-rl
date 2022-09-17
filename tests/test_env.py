import unittest
import numpy as np
import networkx as nx
from src.environment import TrapTheCat

class TestEnv(unittest.TestCase):

    '''
    Test the different functionalities available for the environment:

    1. Generate the env in graph mode
    2. Generate the env in grid mode
    3. A random number < grid_size of cells is blocked
    4. The cat is spawned
    5. The cat does not spawn in the same place as a blocked cell
    6. The cat moves to the closest open edge
    7. The cat moves randomly
    8. Game ends when cat reaches border
    9. Nodes have the following attributes: x, y, blocked, edge 
    10. Test sparse reward (sequence of 0s until either -1 for a loss or +1 for a win)
    
    '''
    def setUp(self) -> None:
        self.env = TrapTheCat()

    def test_graph_mode(self): pass

    def test_grid_mode(self):

        x, y, z = self.env.grid.shape

        self.assertEqual(x, 11)
        self.assertEqual(y,11)
        self.assertEqual(z,2)

    def test_total_cells_blocked(self):

        #Channel 0 is for blocked cells, channel 1 is for cat position
        blocked_cells = self.env.grid[:,:,0].sum()

        self.assertEqual(blocked_cells, 12)

    def test_cat_spawn(self):
        grid = self.env.grid
        x, y = self.env.spawn_cat(grid)

        #Make sure cat's position isn't in a blocked cell
        self.assertEqual(grid[x,y,0], 0)
        self.assertEqual(grid[:,:,1].sum(), 1)

        print(grid[:,:,1])

    def test_cat_good_move(self): pass

    def test_cat_random_move(self): pass

    def test_end_of_episode(self): pass

    def test_sparse_reward(self): pass

    def test_node_attributes(self): pass