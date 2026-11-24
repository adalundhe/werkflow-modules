from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class LakeFormationGetLFTagResponse(BaseModel):
    CatalogId: StrictStr | None = None
    TagKey: StrictStr | None = None
    TagValues: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
