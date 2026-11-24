from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsMskClusterClusterInfoEncryptionInfoEncryptionAtRestDetails(BaseModel):
    DataVolumeKMSKeyId: StrictStr | None = None
