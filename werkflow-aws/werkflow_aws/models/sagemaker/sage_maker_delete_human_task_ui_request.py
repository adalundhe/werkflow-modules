from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteHumanTaskUiRequest(BaseModel):
    HumanTaskUiName: StrictStr
