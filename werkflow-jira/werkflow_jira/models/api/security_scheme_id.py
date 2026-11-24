from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr


class SecuritySchemeId(BaseModel):
    model_config = ConfigDict(extra="allow")

    id: StrictStr | None = None
