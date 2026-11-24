from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeDescribeBatchInferenceJobRequest(BaseModel):
    batchInferenceJobArn: StrictStr
