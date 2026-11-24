from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class IAMListAccountAliasesResponse(BaseModel):
    AccountAliases: list[StrictStr] | None = None
    IsTruncated: StrictBool | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
