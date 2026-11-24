from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class TextractCreateAdapterVersionResponse(BaseModel):
    AdapterId: StrictStr | None = None
    AdapterVersion: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
