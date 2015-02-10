##    pygame - Python Game Library
##    Copyright (C) 2000-2001  Pete Shinners
##
##    This library is free software; you can redistribute it and/or
##    modify it under the terms of the GNU Library General Public
##    License as published by the Free Software Foundation; either
##    version 2 of the License, or (at your option) any later version.
##
##    This library is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
##    Library General Public License for more details.
##
##    You should have received a copy of the GNU Library General Public
##    License along with this library; if not, write to the Free
##    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
##
##    Pete Shinners
##    pete@shinners.org
"""Pygame is a set of Python modules designed for writing games.
It is written on top of the excellent SDL library. This allows you
to create fully featured games and multimedia programs in the python
language. The package is highly portable, with games running on
Windows, MacOS, OS X, BeOS, FreeBSD, IRIX, and Linux.
"""

import sys, os, string

# check if is old windows... if so use directx video driver by default.
# if someone sets this respect their setting...
if not 'SDL_VIDEODRIVER' in os.environ:
    # http://docs.python.org/lib/module-sys.html
    # 0 (VER_PLATFORM_WIN32s) 	Win32s on Windows 3.1
    # 1 (VER_PLATFORM_WIN32_WINDOWS) 	Windows 95/98/ME
    # 2 (VER_PLATFORM_WIN32_NT) 	Windows NT/2000/XP
    # 3 (VER_PLATFORM_WIN32_CE) 	Windows CE
    if hasattr(sys, "getwindowsversion"):
        try:
            if (sys.getwindowsversion()[3] in [1,2] and
                sys.getwindowsversion()[0] in [0,1,2,3,4,5]):
                os.environ['SDL_VIDEODRIVER'] = 'directx'
        except:
            pass

#first, the "required" modules
from pygame.base import *

try: import pygame.event
except (ImportError,IOError):event=MissingModule("event", geterror(), 1)

try: import pygame.joystick
except (ImportError,IOError):joystick=MissingModule("joystick", geterror(), 1)
