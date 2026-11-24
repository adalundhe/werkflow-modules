from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .ssm_attachments_source import SSMAttachmentsSource


class SSMUpdateDocumentRequest(BaseModel):
    Content: StrictStr
    Name: StrictStr
    Attachments: list[SSMAttachmentsSource] | None = None
    DisplayName: StrictStr | None = None
    VersionName: StrictStr | None = None
    DocumentVersion: StrictStr | None = None
    DocumentFormat: Literal['YAML', 'JSON', 'TEXT'] | None = None
    TargetType: StrictStr | None = None
    CloudProviders: list[Literal['AWS', 'Azure', 'GCP']] | None = None
