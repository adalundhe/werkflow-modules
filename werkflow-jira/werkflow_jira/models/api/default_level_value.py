from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr


class DefaultLevelValue(BaseModel):
    model_config = ConfigDict(extra="allow")

    defaultLevelId: StrictStr | None = None
    issueSecuritySchemeId: StrictStr | None = None
