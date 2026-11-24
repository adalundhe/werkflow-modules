from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailContainerServiceStateDetail(BaseModel):
    code: StrictStr | None = None
    message: StrictStr | None = None
