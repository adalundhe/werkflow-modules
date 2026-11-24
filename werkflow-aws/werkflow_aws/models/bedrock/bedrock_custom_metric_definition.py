from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bedrock_rating_scale_item import BedrockRatingScaleItem


class BedrockCustomMetricDefinition(BaseModel):
    name: StrictStr | None = None
    instructions: StrictStr | None = None
    ratingScale: list[BedrockRatingScaleItem] | None = None
