from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BedrockEvaluationDatasetLocation(BaseModel):
    s3Uri: StrictStr | None = None
