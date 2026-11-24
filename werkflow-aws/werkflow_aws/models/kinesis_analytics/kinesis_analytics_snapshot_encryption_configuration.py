from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsSnapshotEncryptionConfiguration(BaseModel):
    KeyId: StrictStr | None = None
    KeyType: StrictStr | None = None
