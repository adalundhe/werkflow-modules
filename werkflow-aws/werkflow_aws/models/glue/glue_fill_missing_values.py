from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueFillMissingValues(BaseModel):
    Name: StrictStr | None = None
    Inputs: list[StrictStr] | None = None
    ImputedPath: StrictStr | None = None
    FilledPath: StrictStr | None = None
