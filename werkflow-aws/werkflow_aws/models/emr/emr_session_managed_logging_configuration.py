from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EMRSessionManagedLoggingConfiguration(BaseModel):
    Enabled: StrictBool | None = None
    EncryptionKeyArn: StrictStr | None = None
