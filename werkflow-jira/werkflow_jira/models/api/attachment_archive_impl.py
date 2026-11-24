from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .attachment_archive_entry import AttachmentArchiveEntry


class AttachmentArchiveImpl(BaseModel):
    entries: list[AttachmentArchiveEntry] | None = None
    totalEntryCount: StrictInt | None = None
