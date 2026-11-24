from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchDataSourceAttachmentSummary(BaseModel):
    attachmentId: StrictStr | None = None
    dataSourceArn: StrictStr | None = None
    status: StrictStr | None = None
