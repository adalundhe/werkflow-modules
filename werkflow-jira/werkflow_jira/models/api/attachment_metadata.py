from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .user import User


class AttachmentMetadata(BaseModel):
    author: User | None = None
    content: StrictStr | None = None
    created: StrictStr | None = None
    filename: StrictStr | None = None
    id: StrictInt | None = None
    mimeType: StrictStr | None = None
    properties: dict[StrictStr, Any] | None = None
    self: StrictStr | None = None
    size: StrictInt | None = None
    thumbnail: StrictStr | None = None
