class WordFinder:
    def set_grid(self,grid):
        self.grid = []
        for element in grid:
            self.grid.append(list(element))
    
    def count(self, word):
        coordinates = [(0,1),
                       ()
                       ]
        
            
if __name__ == "__main__":
    grid = ["TIRATIRA",
            "IRATIRAT",
            "RATIRATI",
            "ATIRATIR"]

    finder = WordFinder()
    print(finder.set_grid(grid)) 