from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class ComprehendEntityLabel(BaseModel):
    Name: StrictStr | None = None
    Score: StrictFloat | StrictInt | None = None
