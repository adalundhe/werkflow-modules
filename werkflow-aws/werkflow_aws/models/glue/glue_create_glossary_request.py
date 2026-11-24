from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueCreateGlossaryRequest(BaseModel):
    Name: StrictStr
    Description: StrictStr | None = None
    ClientToken: StrictStr | None = None
