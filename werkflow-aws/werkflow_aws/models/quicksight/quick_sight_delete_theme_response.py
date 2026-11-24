from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightDeleteThemeResponse(BaseModel):
    Arn: StrictStr | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ThemeId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
