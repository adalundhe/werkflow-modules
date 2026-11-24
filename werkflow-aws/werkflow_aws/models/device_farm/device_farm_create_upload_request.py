from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmCreateUploadRequest(BaseModel):
    projectArn: StrictStr
    name: StrictStr
    type: StrictStr
    contentType: StrictStr | None = None
