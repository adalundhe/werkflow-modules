from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class StorageGatewayVolumeiSCSIAttributes(BaseModel):
    TargetARN: StrictStr | None = None
    NetworkInterfaceId: StrictStr | None = None
    NetworkInterfacePort: StrictInt | None = None
    LunNumber: StrictInt | None = None
    ChapEnabled: StrictBool | None = None
