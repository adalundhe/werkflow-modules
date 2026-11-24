from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueCreateGlossaryTermRequest(BaseModel):
    GlossaryIdentifier: StrictStr
    Name: StrictStr
    ShortDescription: StrictStr | None = None
    LongDescription: StrictStr | None = None
    ClientToken: StrictStr | None = None
