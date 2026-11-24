from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt
from .attachment_archive_entry import AttachmentArchiveEntry


class AttachmentArchive(BaseModel):
    entries: list[AttachmentArchiveEntry] | None = None
    moreAvailable: StrictBool | None = None
    totalEntryCount: StrictInt | None = None
    totalNumberOfEntriesAvailable: StrictInt | None = None
