from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockEvaluationOutputDataConfig(BaseModel):
    s3Uri: StrictStr | None = None
