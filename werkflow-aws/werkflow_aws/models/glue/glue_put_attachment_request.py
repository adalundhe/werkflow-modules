from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GluePutAttachmentRequest(BaseModel):
    AssetIdentifier: StrictStr
    AttachmentName: StrictStr
    Content: StrictStr
    IterableFormName: StrictStr | None = None
    ItemIdentifier: StrictStr | None = None
    FormTypeIdentifier: StrictStr | None = None
    ClientToken: StrictStr | None = None
