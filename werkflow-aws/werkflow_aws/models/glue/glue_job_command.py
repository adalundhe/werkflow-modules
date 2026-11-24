from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueJobCommand(BaseModel):
    Name: StrictStr | None = None
    ScriptLocation: StrictStr | None = None
    PythonVersion: StrictStr | None = None
    Runtime: StrictStr | None = None
