from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RDSOutpostModel(BaseModel):
    Arn: StrictStr | None = None
