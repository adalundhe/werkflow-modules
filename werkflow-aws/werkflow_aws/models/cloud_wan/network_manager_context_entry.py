from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerContextEntry(BaseModel):
    ContextId: StrictStr | None = None
    ContextType: StrictStr | None = None
    SegmentType: StrictStr | None = None
    PublicId: StrictStr | None = None
    Region: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    AttachmentType: StrictStr | None = None
