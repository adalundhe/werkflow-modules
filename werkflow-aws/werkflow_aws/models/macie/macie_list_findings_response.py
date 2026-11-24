from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class MacieListFindingsResponse(BaseModel):
    findingIds: list[StrictStr] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
