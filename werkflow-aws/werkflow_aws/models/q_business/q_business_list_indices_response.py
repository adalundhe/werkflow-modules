from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .q_business_index import QBusinessIndex


class QBusinessListIndicesResponse(BaseModel):
    nextToken: StrictStr | None = None
    indices: list[QBusinessIndex] | None = None
    ResponseMetadata: dict[str, Any] | None = None
