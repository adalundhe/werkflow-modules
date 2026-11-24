from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PersonalizeDescribeBatchSegmentJobRequest(BaseModel):
    batchSegmentJobArn: StrictStr
