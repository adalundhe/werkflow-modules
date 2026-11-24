from __future__ import annotations
from typing import Literal


SageMakerAthenaResultFormat = Literal[
    'PARQUET',
    'ORC',
    'AVRO',
    'JSON',
    'TEXTFILE',
]
