from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsApplicationEncryptionConfigurationDescription(BaseModel):
    KeyId: StrictStr | None = None
    KeyType: StrictStr | None = None
