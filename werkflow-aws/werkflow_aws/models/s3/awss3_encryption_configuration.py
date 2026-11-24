from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .awss3_use_source_multi_region_key import AWSS3UseSourceMultiRegionKey


class AWSS3EncryptionConfiguration(BaseModel):
    ReplicaKmsKeyID: StrictStr | None = None
    UseSourceMultiRegionKey: AWSS3UseSourceMultiRegionKey | None = None
