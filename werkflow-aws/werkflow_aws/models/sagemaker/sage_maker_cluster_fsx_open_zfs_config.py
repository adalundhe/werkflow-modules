from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerClusterFsxOpenZfsConfig(BaseModel):
    DnsName: StrictStr | None = None
    MountPath: StrictStr | None = None
