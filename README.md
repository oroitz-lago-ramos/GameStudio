# GameStudio
wow

NOM des settings utiliser pour le raycasting:

#Settings
resX = 1920 
resY = 1080
HALF_WIDTH = resX // 2
HALF_HEIGHT = resY // 2
ECHELLE = 100 

# player settings
player_pos = (1, 1)
player_angle = 0
vitesse = 4

# ray casting settings
FOV = np.pi / 3  
HALF_FOV = FOV / 2
NUM_RAYS = 80
MAX_DEPTH = 2000
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * np.tan(HALF_FOV))
WALL_HEIGHT = 4 * DIST * ECHELLE
SCALE = resX // NUM_RAYS  
