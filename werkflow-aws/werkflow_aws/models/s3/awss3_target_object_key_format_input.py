from __future__ import annotations
from pydantic import BaseModel
from .awss3_partitioned_prefix_input import AWSS3PartitionedPrefixInput
from .awss3_simple_prefix_input import AWSS3SimplePrefixInput


class AWSS3TargetObjectKeyFormatInput(BaseModel):
    SimplePrefix: AWSS3SimplePrefixInput | None = None
    PartitionedPrefix: AWSS3PartitionedPrefixInput | None = None
