from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EMRCommand(BaseModel):
    Name: StrictStr | None = None
    ScriptPath: StrictStr | None = None
    Args: list[StrictStr] | None = None
