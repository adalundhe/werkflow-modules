from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DeviceFarmUpdateUploadRequest(BaseModel):
    arn: StrictStr
    name: StrictStr | None = None
    contentType: StrictStr | None = None
    editContent: StrictBool | None = None
