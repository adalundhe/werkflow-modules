from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LightsailInstanceState(BaseModel):
    code: StrictInt | None = None
    name: StrictStr | None = None
