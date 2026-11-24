from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCatalystIdeConfiguration(BaseModel):
    runtime: StrictStr | None = None
    name: StrictStr | None = None
