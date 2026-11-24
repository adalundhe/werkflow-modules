from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KinesisAnalyticsEncryptionConfigurationDescription(BaseModel):
    KeyId: StrictStr | None = None
    KeyType: StrictStr | None = None
