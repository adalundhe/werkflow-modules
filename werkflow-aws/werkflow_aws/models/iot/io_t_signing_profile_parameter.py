from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTSigningProfileParameter(BaseModel):
    certificateArn: StrictStr | None = None
    platform: StrictStr | None = None
    certificatePathOnDevice: StrictStr | None = None
