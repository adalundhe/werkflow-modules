from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .board_feature_payload import BoardFeaturePayload


class BoardFeaturesPayload(BaseModel):
    boardFeatures: dict[StrictStr, list[BoardFeaturePayload]] | None = None
