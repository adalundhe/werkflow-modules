from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SSMGetDeployablePatchSnapshotForInstanceResponse(BaseModel):
    InstanceId: StrictStr | None = None
    SnapshotId: StrictStr | None = None
    SnapshotDownloadUrl: StrictStr | None = None
    Product: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
