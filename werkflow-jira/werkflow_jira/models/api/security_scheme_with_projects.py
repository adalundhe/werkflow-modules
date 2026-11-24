from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr


class SecuritySchemeWithProjects(BaseModel):
    model_config = ConfigDict(extra="allow")

    defaultLevel: StrictInt | None = None
    description: StrictStr | None = None
    id: StrictInt | None = None
    name: StrictStr | None = None
    projectIds: list[StrictInt] | None = None
    self: StrictStr | None = None
