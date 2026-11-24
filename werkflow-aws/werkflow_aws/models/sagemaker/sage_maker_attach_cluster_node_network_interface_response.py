from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SageMakerAttachClusterNodeNetworkInterfaceResponse(BaseModel):
    ClusterArn: StrictStr | None = None
    NodeId: StrictStr | None = None
    NetworkInterfaceId: StrictStr | None = None
    AttachmentId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
