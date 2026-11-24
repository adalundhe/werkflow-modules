from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AttachmentArchiveItemReadable(BaseModel):
    index: StrictInt | None = None
    label: StrictStr | None = None
    mediaType: StrictStr | None = None
    path: StrictStr | None = None
    size: StrictStr | None = None
