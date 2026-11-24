from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRS3MonitoringConfiguration(BaseModel):
    LogUri: StrictStr | None = None
    EncryptionKeyArn: StrictStr | None = None
