from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeleteContextRequest(BaseModel):
    ContextName: StrictStr
