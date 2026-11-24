from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerAttachmentError(BaseModel):
    Code: StrictStr | None = None
    Message: StrictStr | None = None
    ResourceArn: StrictStr | None = None
    RequestId: StrictStr | None = None
