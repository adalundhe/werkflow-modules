from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueRenameField(BaseModel):
    Name: StrictStr | None = None
    Inputs: list[StrictStr] | None = None
    SourcePath: list[StrictStr] | None = None
    TargetPath: list[StrictStr] | None = None
