from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaOnFailureModel(BaseModel):
    Destination: StrictStr | None = None
