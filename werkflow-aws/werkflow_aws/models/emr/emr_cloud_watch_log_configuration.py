from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EMRCloudWatchLogConfiguration(BaseModel):
    Enabled: StrictBool | None = None
    LogGroupName: StrictStr | None = None
    LogStreamNamePrefix: StrictStr | None = None
    EncryptionKeyArn: StrictStr | None = None
    LogTypes: dict[StrictStr, list[StrictStr]] | None = None
