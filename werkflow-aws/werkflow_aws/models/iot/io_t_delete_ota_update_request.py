from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class IoTDeleteOTAUpdateRequest(BaseModel):
    otaUpdateId: StrictStr
    deleteStream: StrictBool | None = None
    forceDeleteAWSJob: StrictBool | None = None
