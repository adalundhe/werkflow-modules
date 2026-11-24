from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockQueryTransformationConfiguration(BaseModel):
    type: StrictStr | None = None
