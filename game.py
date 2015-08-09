import pygame
import time

from src.constants import *
from src.menus.TitleScene import TitleScene
from src.Event import Event

def main():

	pygame.init()
	real_screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	virtual_screen = pygame.Surface((GAME_WIDTH, GAME_HEIGHT))
	active_scene = TitleScene()
	
	mouse_pos = (0, 0)
	counter = 0
	while True:
		
		begin = time.time()
		
		events = []
		for e in pygame.event.get():
			if e.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = e.pos
				x, y = mouse_pos
				events.append(Event('mousedown', x, y, e.button == 1))
			elif e.type == pygame.MOUSEBUTTONUP:
				mouse_pos = e.pos
				x, y = mouse_pos
				events.append(Event('mouseup', x, y, e.button == 1))
			elif e.type == pygame.MOUSEMOTION:
				mouse_pos = e.pos
				x, y = mouse_pos
				events.append(Event('mousemove', x, y, False))
			elif e.type == pygame.QUIT:
				return
			elif e.type == pygame.KEYDOWN:
				pressed_keys = pygame.key.get_pressed()
				
				if e.key == pygame.K_F4 and (pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT]):
					return
				elif e.key == pygame.K_w and (pressed_keys[pygame.K_LCTRL] or pressed_keys[pygame.K_RCTRL]):
					return
				elif e.key == pygame.K_ESCAPE:
					return
		
		active_scene.update(events, mouse_pos)
		active_scene.render(virtual_screen, counter)
		
		pygame.transform.scale(virtual_screen, real_screen.get_size(), real_screen)
		
		pygame.display.flip()
		
		next_scene = active_scene.next
		if next_scene != None:
			active_scene.next = None
			active_scene = next_scene
		
		if active_scene == None:
			return
		
		counter += 1
		
		end = time.time()
		
		diff = end - begin
		delay = 1.0 / FPS
		wait = delay - diff
		if wait > 0:
			time.sleep(wait)

main()