from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .open_search_data_source_attachment_summary import OpenSearchDataSourceAttachmentSummary


class OpenSearchListDataSourceAttachmentsResponse(BaseModel):
    attachments: list[OpenSearchDataSourceAttachmentSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
