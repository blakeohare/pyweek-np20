from src.PlayBoard import PlayBoard
from src.Model import Model

class PlayScene:
	def __init__(self):
		self.next = None
		self.model = Model()
		self.board = PlayBoard()
	
	def update(self, events, mouse_coords):
		pass
	
	def render(self, screen, rc):
		screen.fill((0, 0, 0))
		
		self.board.render(screen, rc, 0, 0, self.model.staff)
		
		