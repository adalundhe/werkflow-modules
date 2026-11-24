from __future__ import annotations
from typing import Literal


SageMakerRedshiftResultCompressionType = Literal[
    'None',
    'GZIP',
    'BZIP2',
    'ZSTD',
    'SNAPPY',
]
