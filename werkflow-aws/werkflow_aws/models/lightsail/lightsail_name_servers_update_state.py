from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailNameServersUpdateState(BaseModel):
    code: StrictStr | None = None
    message: StrictStr | None = None
