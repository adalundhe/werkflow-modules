from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kms_multi_region_key import KMSMultiRegionKey


class KMSMultiRegionConfiguration(BaseModel):
    MultiRegionKeyType: StrictStr | None = None
    PrimaryKey: KMSMultiRegionKey | None = None
    ReplicaKeys: list[KMSMultiRegionKey] | None = None
