from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerClusterFsxLustreConfig(BaseModel):
    DnsName: StrictStr | None = None
    MountName: StrictStr | None = None
    MountPath: StrictStr | None = None
