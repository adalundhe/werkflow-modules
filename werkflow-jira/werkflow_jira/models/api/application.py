from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr


class Application(BaseModel):
    model_config = ConfigDict(extra="allow")

    name: StrictStr | None = None
    type: StrictStr | None = None
