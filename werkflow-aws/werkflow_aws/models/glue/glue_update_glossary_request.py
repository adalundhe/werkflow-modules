from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueUpdateGlossaryRequest(BaseModel):
    Identifier: StrictStr
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    ClientToken: StrictStr | None = None
