from __future__ import annotations
from typing import Literal


SageMakerVariantStatus = Literal[
    'Creating',
    'Updating',
    'Deleting',
    'ActivatingTraffic',
    'Baking',
]
