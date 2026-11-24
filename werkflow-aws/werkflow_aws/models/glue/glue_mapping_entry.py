from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueMappingEntry(BaseModel):
    SourceTable: StrictStr | None = None
    SourcePath: StrictStr | None = None
    SourceType: StrictStr | None = None
    TargetTable: StrictStr | None = None
    TargetPath: StrictStr | None = None
    TargetType: StrictStr | None = None
