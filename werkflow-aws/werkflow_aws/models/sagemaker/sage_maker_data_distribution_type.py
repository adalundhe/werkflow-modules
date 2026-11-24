from __future__ import annotations
from typing import Literal


SageMakerDataDistributionType = Literal[
    'FullyReplicated',
    'ShardedByS3Key',
]
