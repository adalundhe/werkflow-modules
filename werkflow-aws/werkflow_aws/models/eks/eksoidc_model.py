from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSOIDCModel(BaseModel):
    issuer: StrictStr | None = None
