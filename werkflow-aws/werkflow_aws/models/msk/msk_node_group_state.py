from typing import Literal


MSKNodeGroupState = Literal[
    'ACTIVE',
    'CREATING',
    'DELETING',
    'FAILED',
    'HEALING',
    'MAINTENANCE',
    'REBOOTING_BROKER',
    'UPDATING',
]