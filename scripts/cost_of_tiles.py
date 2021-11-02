#Find Cost of Tile to Cover W x H Floor - Calculate the total cost of tile it would take to cover a floor plan of width and height, using a cost entered by the user.
import math

def calculate_no_of_tiles(floor_dimensions, tile_dimensions, cost_per_tile):
  """
  A program to calculate total cost of tile it would take to cover a floor plan of (width, height) dimensions
  :param tuple floor_dimensions: tuple or list of width and height dimensions of the floor
  :param tuple tile_dimensions: tuple or list of width and height dimensions of the tile
  :param float cost_per_tile: cost per tile of a given dimensions
  :return float: total cost of the tiles required to fill the floor plan
  """
  f_width, f_height = floor_dimensions
  t_width, t_height = tile_dimensions
  floor_area = f_width * f_height
  tile_area = t_width * t_height
  no_of_tiles_required = math.ceil(floor_area / tile_area)
  return no_of_tiles_required * cost_per_tile

print(calculate_no_of_tiles((9, 4.5), (2, 1.5), 100))
print(calculate_no_of_tiles((10, 10), (2, 2), 100))
print(calculate_no_of_tiles((13, 6.5), (1, 1), 100))
calculate_no_of_tiles()