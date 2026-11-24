from __future__ import annotations
from pydantic import BaseModel, StrictBool


class SageMakerModelAccessConfigModel(BaseModel):
    AcceptEula: StrictBool | None = None
