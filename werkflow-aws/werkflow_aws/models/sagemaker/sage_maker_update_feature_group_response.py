from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class SageMakerUpdateFeatureGroupResponse(BaseModel):
    FeatureGroupArn: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
