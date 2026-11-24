from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_rating_scale_item_value import BedrockRatingScaleItemValue


class BedrockRatingScaleItem(BaseModel):
    definition: StrictStr | None = None
    value: BedrockRatingScaleItemValue | None = None
