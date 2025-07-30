from typing import Literal


AthenaQueryState = Literal[
    'QUEUED',
    'RUNNING',
    'SUCCEEDED',
    'FAILED',
    'CANCELLED',
]