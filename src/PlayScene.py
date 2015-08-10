from src.PlayBoard import PlayBoard
from src.Model import Model

class PlayScene:
	def __init__(self, level_id):
		self.next = None
		self.model = Model(level_id)
		self.board = PlayBoard(self.model)
	
	def update(self, events, mouse_coords):
		self.board.update(events)
	
	def render(self, screen, rc):
		screen.fill((0, 0, 0))
		
		self.board.render(screen, rc, 0, 0, self.model.staff)
		
		