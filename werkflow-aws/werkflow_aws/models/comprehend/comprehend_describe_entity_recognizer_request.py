from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendDescribeEntityRecognizerRequest(BaseModel):
    EntityRecognizerArn: StrictStr
