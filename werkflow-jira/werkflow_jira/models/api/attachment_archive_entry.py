from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AttachmentArchiveEntry(BaseModel):
    abbreviatedName: StrictStr | None = None
    entryIndex: StrictInt | None = None
    mediaType: StrictStr | None = None
    name: StrictStr | None = None
    size: StrictInt | None = None
