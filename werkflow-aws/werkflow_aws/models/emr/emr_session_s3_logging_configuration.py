from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EMRSessionS3LoggingConfiguration(BaseModel):
    Enabled: StrictBool | None = None
    LogUri: StrictStr | None = None
    EncryptionKeyArn: StrictStr | None = None
    LogTypes: dict[StrictStr, list[StrictStr]] | None = None
