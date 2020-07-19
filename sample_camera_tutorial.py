#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  sample_camera_tutorial.py
#  
#  Copyright 2019  <pi@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    import pygame
    import pygame.camera
    from pygame.locals import *

    pygame.init()
    pygame.camera.init()
    pygame.camera.list_cameras()
    
    cam = pygame.camera.Camera("/dev/video0",(640,480))
    cam = pygame.camera.Camera(pygame.camera.list_cameras()[0])
    cam.start()
    image = cam.get_image()
    
    sys.exit(main(sys.argv))

