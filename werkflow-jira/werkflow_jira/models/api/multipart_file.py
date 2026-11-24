from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .resource import Resource


class MultipartFile(BaseModel):
    bytes: list[StrictStr] | None = None
    contentType: StrictStr | None = None
    empty: StrictBool | None = None
    inputStream: dict[StrictStr, Any] | None = None
    name: StrictStr | None = None
    originalFilename: StrictStr | None = None
    resource: Resource | None = None
    size: StrictInt | None = None
