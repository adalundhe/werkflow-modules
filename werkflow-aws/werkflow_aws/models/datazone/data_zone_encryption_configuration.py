from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneEncryptionConfiguration(BaseModel):
    kmsKeyArn: StrictStr | None = None
    sseAlgorithm: StrictStr | None = None
