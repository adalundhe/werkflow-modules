from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueSessionCommand(BaseModel):
    Name: StrictStr | None = None
    PythonVersion: StrictStr | None = None
