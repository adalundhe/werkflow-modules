from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockRequestMetadataBaseFilters(BaseModel):
    equals: dict[StrictStr, StrictStr] | None = None
    notEquals: dict[StrictStr, StrictStr] | None = None
