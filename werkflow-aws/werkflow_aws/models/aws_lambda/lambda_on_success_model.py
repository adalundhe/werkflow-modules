from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaOnSuccessModel(BaseModel):
    Destination: StrictStr | None = None
