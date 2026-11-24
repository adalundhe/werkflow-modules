from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaOnFailure(BaseModel):
    Destination: StrictStr | None = None
