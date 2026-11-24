from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteActionRequest(BaseModel):
    ActionName: StrictStr
