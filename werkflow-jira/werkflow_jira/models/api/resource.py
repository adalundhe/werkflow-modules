from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class Resource(BaseModel):
    contentAsByteArray: list[StrictStr] | None = None
    description: StrictStr | None = None
    file: StrictStr | None = None
    filename: StrictStr | None = None
    inputStream: dict[StrictStr, Any] | None = None
    open: StrictBool | None = None
    readable: StrictBool | None = None
    uri: StrictStr | None = None
    url: StrictStr | None = None
