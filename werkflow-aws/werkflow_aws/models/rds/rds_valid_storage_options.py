from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .rds_double_range import RDSDoubleRange
from .rds_range import RDSRange


class RDSValidStorageOptions(BaseModel):
    StorageType: StrictStr | None = None
    StorageSize: list[RDSRange] | None = None
    ProvisionedIops: list[RDSRange] | None = None
    IopsToStorageRatio: list[RDSDoubleRange] | None = None
    ProvisionedStorageThroughput: list[RDSRange] | None = None
    StorageThroughputToIopsRatio: list[RDSDoubleRange] | None = None
    SupportsStorageAutoscaling: StrictBool | None = None
