from __future__ import annotations
from typing import Literal


DynamoDBVectorDistanceFunction = Literal[
    'COSINE',
    'DOT_PRODUCT',
    'EUCLIDEAN',
]
