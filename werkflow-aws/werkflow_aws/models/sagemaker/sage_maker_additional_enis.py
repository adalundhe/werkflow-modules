from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerAdditionalEnis(BaseModel):
    EfaEnis: list[StrictStr] | None = None
