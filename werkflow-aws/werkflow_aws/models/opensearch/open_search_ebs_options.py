from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class OpenSearchEBSOptions(BaseModel):
    EBSEnabled: StrictBool | None = None
    VolumeType: StrictStr | None = None
    VolumeSize: StrictInt | None = None
    Iops: StrictInt | None = None
    Throughput: StrictInt | None = None
