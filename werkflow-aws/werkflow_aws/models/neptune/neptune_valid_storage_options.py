from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .neptune_double_range import NeptuneDoubleRange
from .neptune_range import NeptuneRange


class NeptuneValidStorageOptions(BaseModel):
    StorageType: StrictStr | None = None
    StorageSize: list[NeptuneRange] | None = None
    ProvisionedIops: list[NeptuneRange] | None = None
    IopsToStorageRatio: list[NeptuneDoubleRange] | None = None
