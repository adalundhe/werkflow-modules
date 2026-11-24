from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_request_metadata_base_filters import BedrockRequestMetadataBaseFilters


class BedrockRequestMetadataFilters(BaseModel):
    equals: dict[StrictStr, StrictStr] | None = None
    notEquals: dict[StrictStr, StrictStr] | None = None
    andAll: list[BedrockRequestMetadataBaseFilters] | None = None
    orAll: list[BedrockRequestMetadataBaseFilters] | None = None
