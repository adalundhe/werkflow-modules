from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .attachment_archive_item_readable import AttachmentArchiveItemReadable


class AttachmentArchiveMetadataReadable(BaseModel):
    entries: list[AttachmentArchiveItemReadable] | None = None
    id: StrictInt | None = None
    mediaType: StrictStr | None = None
    name: StrictStr | None = None
    totalEntryCount: StrictInt | None = None
