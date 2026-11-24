from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ComprehendStopTrainingEntityRecognizerRequest(BaseModel):
    EntityRecognizerArn: StrictStr
