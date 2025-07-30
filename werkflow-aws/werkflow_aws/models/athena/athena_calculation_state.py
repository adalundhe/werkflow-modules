from typing import Literal


AthenaCalculationState = Literal[
    'CREATING',
    'CREATED',
    'QUEUED',
    'RUNNING',
    'CANCELING',
    'CANCELED',
    'COMPLETED',
    'FAILED',
]