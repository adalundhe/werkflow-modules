from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SNSPlatformApplication(BaseModel):
    PlatformApplicationArn: StrictStr | None = None
    Attributes: dict[StrictStr, StrictStr] | None = None
