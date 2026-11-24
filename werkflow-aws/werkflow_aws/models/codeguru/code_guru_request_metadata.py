from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_guru_event_info import CodeGuruEventInfo


class CodeGuruRequestMetadata(BaseModel):
    RequestId: StrictStr | None = None
    Requester: StrictStr | None = None
    EventInfo: CodeGuruEventInfo | None = None
    VendorName: StrictStr | None = None
