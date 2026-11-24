from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceConformancePackSource(BaseModel):
    SourceIdentifier: StrictStr | None = None
