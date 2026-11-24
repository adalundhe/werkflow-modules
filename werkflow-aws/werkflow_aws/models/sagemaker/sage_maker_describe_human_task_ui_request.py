from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDescribeHumanTaskUiRequest(BaseModel):
    HumanTaskUiName: StrictStr
