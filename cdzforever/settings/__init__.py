# -*- coding: utf-8 -*-

import platform

if platform.node() in ['Aiur', 'belize']:
    from local import *
else:
    from prod import *
