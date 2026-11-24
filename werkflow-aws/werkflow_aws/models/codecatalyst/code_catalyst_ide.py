from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCatalystIde(BaseModel):
    runtime: StrictStr | None = None
    name: StrictStr | None = None
