from __future__ import annotations
from pydantic import BaseModel, StrictBool


class SageMakerModelAccessConfig(BaseModel):
    AcceptEula: StrictBool | None = None
