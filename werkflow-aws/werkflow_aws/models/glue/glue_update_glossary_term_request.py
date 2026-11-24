from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueUpdateGlossaryTermRequest(BaseModel):
    Identifier: StrictStr
    Name: StrictStr | None = None
    ShortDescription: StrictStr | None = None
    LongDescription: StrictStr | None = None
    ClientToken: StrictStr | None = None
