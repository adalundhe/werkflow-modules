from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr


class ComponentJsonBean(BaseModel):
    model_config = ConfigDict(extra="allow")

    ari: StrictStr | None = None
    description: StrictStr | None = None
    id: StrictStr | None = None
    metadata: dict[StrictStr, StrictStr] | None = None
    name: StrictStr | None = None
    self: StrictStr | None = None
