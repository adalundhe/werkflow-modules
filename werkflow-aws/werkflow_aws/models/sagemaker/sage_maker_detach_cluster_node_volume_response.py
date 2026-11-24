from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class SageMakerDetachClusterNodeVolumeResponse(BaseModel):
    ClusterArn: StrictStr | None = None
    NodeId: StrictStr | None = None
    VolumeId: StrictStr | None = None
    AttachTime: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    DeviceName: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
