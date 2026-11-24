from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class LakeFormationDeleteDataCellsFilterResponse(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None
