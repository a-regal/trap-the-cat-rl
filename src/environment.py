from re import T
import numpy as np


np.random.seed(42)

class TrapTheCat():
    def __init__(self, grid_size=11, graph_mode=False, random_cat=True, render_mode=None, cells_to_block=12):
        '''
        Trap the cat environment, designed on the basis of an OpenAI gym env.

        Defaults:

        grid_size = 11. Create an 11x11 grid
        graph_mode = False. Create a straight grid by default
        random_cat = True. Move the cat at random to x,y positions
        render_mode = None. Default to None since agent visuals aren't being used yet.
        cells_to_block = 12. 10% of the grid is blocked

        '''

        self.cells_to_block = cells_to_block
        self.random_cat = random_cat
        self.graph_mode = graph_mode
        
        self.grid = self.setup_grid(grid_size)


    def get_block_cells_indices(self):
        #1. Generate an array of cells_to_block x 2
        return np.random.randint(0,11, size=(self.cells_to_block,2))

    def setup_grid(self, grid_size):
        #Create grid of zeros
        grid = np.zeros((grid_size, grid_size, 2))

        #Get indices to block
        idx = self.get_block_cells_indices()

        #Setup blocked cells
        grid[idx[:,0], idx[:,1], 0] = 1

        # #Spawn cat
        cat_position = self.spawn_cat(grid)

        grid[cat_position[0], cat_position[1], 1] = 1

        return grid

    def spawn_cat(self, grid):
        '''
        Return the index of the cat spawn
        '''

        available = np.vstack(np.where(grid[:,:,0] != 1)).T
        cat_position = np.random.choice(available.shape[0])

        return available[cat_position, :]

