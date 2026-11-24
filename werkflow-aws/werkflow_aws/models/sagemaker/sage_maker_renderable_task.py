from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerRenderableTask(BaseModel):
    Input: StrictStr
