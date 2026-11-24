from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .support_attachment import SupportAttachment


class SupportDescribeAttachmentResponse(BaseModel):
    attachment: SupportAttachment | None = None
    ResponseMetadata: dict[str, Any] | None = None
