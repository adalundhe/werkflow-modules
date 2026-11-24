from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildFleetProxyRule(BaseModel):
    type: StrictStr | None = None
    effect: StrictStr | None = None
    entities: list[StrictStr] | None = None
