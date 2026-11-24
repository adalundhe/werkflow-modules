from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchDomainNodesStatus(BaseModel):
    NodeId: StrictStr | None = None
    NodeType: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    InstanceType: StrictStr | None = None
    NodeStatus: StrictStr | None = None
    StorageType: StrictStr | None = None
    StorageVolumeType: StrictStr | None = None
    StorageSize: StrictStr | None = None
