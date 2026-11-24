from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .q_business_copy_from_source import QBusinessCopyFromSource
from .q_business_error_detail import QBusinessErrorDetail


class QBusinessAttachment(BaseModel):
    attachmentId: StrictStr | None = None
    conversationId: StrictStr | None = None
    name: StrictStr | None = None
    copyFrom: QBusinessCopyFromSource | None = None
    fileType: StrictStr | None = None
    fileSize: StrictInt | None = None
    md5chksum: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    status: StrictStr | None = None
    error: QBusinessErrorDetail | None = None
