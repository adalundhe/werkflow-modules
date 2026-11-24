from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDeleteAttachmentRequest(BaseModel):
    AssetIdentifier: StrictStr
    AttachmentName: StrictStr
    IterableFormName: StrictStr | None = None
    ItemIdentifier: StrictStr | None = None
