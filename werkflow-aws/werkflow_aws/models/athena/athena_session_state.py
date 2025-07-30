from typing import Literal


AthenaSessionState = Literal[
    'CREATING',
    'CREATED',
    'IDLE',
    'BUSY',
    'TERMINATING',
    'TERMINATED',
    'DEGRADED',
    'FAILED',
]