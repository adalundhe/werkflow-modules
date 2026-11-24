from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCatalystSpaceSummary(BaseModel):
    name: StrictStr | None = None
    regionName: StrictStr | None = None
    displayName: StrictStr | None = None
    description: StrictStr | None = None
