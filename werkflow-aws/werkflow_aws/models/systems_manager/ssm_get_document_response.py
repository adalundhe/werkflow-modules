from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .ssm_attachment_content import SSMAttachmentContent
from .ssm_document_requires import SSMDocumentRequires


class SSMGetDocumentResponse(BaseModel):
    Name: StrictStr | None = None
    CreatedDate: datetime.datetime | StrictStr | None = None
    DisplayName: StrictStr | None = None
    VersionName: StrictStr | None = None
    DocumentVersion: StrictStr | None = None
    Status: StrictStr | None = None
    StatusInformation: StrictStr | None = None
    Content: StrictStr | None = None
    DocumentType: StrictStr | None = None
    DocumentFormat: StrictStr | None = None
    Requires: list[SSMDocumentRequires] | None = None
    AttachmentsContent: list[SSMAttachmentContent] | None = None
    ReviewStatus: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
