from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EMRSessionCloudWatchLoggingConfiguration(BaseModel):
    Enabled: StrictBool | None = None
    LogGroup: StrictStr | None = None
    LogStreamNamePrefix: StrictStr | None = None
    EncryptionKeyArn: StrictStr | None = None
    LogTypes: dict[StrictStr, list[StrictStr]] | None = None
