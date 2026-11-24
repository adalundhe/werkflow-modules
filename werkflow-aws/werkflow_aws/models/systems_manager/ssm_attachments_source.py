from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SSMAttachmentsSource(BaseModel):
    Key: Literal['SourceUrl', 'S3FileUrl', 'AttachmentReference'] | None = None
    Values: list[StrictStr] | None = None
    Name: StrictStr | None = None
