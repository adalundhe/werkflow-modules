from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class BoardFeaturePayload(BaseModel):
    featureKey: StrictStr | None = None
    state: StrictBool | None = None
