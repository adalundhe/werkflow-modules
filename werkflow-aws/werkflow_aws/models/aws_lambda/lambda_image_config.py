from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaImageConfig(BaseModel):
    EntryPoint: list[StrictStr] | None = None
    Command: list[StrictStr] | None = None
    WorkingDirectory: StrictStr | None = None
