from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMResourceDataSyncDestinationDataSharing(BaseModel):
    DestinationDataSharingType: StrictStr | None = None
