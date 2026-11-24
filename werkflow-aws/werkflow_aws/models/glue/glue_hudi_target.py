from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlueHudiTarget(BaseModel):
    Paths: list[StrictStr] | None = None
    ConnectionName: StrictStr | None = None
    Exclusions: list[StrictStr] | None = None
    MaximumTraversalDepth: StrictInt | None = None
