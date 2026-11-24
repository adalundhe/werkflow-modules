from __future__ import annotations
from pydantic import BaseModel
from .awss3_partitioned_prefix import AWSS3PartitionedPrefix
from .awss3_simple_prefix import AWSS3SimplePrefix


class AWSS3TargetObjectKeyFormat(BaseModel):
    SimplePrefix: AWSS3SimplePrefix | None = None
    PartitionedPrefix: AWSS3PartitionedPrefix | None = None
