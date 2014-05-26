# -*- coding: utf-8 -*-

import platform

if platform.node() == 'Aiur':
    from local import *
else:
    from prod import *
