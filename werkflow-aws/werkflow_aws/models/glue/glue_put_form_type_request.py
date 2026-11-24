from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GluePutFormTypeRequest(BaseModel):
    Name: StrictStr
    Schema: StrictStr
    ClientToken: StrictStr | None = None
