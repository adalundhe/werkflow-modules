from __future__ import annotations
from typing import Literal


SageMakerS3DataDistribution = Literal[
    'FullyReplicated',
    'ShardedByS3Key',
]
