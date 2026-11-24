from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteAppImageConfigRequest(BaseModel):
    AppImageConfigName: StrictStr
