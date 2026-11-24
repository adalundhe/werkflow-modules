from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectRealTimeContactAnalysisAttachment(BaseModel):
    AttachmentName: StrictStr | None = None
    ContentType: StrictStr | None = None
    AttachmentId: StrictStr | None = None
    Status: StrictStr | None = None
