from __future__ import annotations
from typing import Literal


SageMakerProcessingS3DataDistributionType = Literal[
    'FullyReplicated',
    'ShardedByS3Key',
]
