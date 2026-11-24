from __future__ import annotations
from pydantic import BaseModel, StrictBool


class SageMakerSessionChainingConfig(BaseModel):
    EnableSessionTagChaining: StrictBool | None = None
