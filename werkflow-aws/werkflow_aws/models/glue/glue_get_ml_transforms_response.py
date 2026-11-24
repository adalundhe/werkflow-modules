from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_ml_transform import GlueMLTransform


class GlueGetMLTransformsResponse(BaseModel):
    Transforms: list[GlueMLTransform] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
