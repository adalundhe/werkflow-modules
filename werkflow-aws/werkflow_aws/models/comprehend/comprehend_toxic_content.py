from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class ComprehendToxicContent(BaseModel):
    Name: StrictStr | None = None
    Score: StrictFloat | StrictInt | None = None
