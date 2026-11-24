from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr


class Visibility(BaseModel):
    model_config = ConfigDict(extra="allow")

    identifier: StrictStr | None = None
    type: StrictStr | None = None
    value: StrictStr | None = None
