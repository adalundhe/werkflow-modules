from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerUiTemplate(BaseModel):
    Content: StrictStr
