from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AthenaApplicationDPUSizes(BaseModel):
    ApplicationRuntimeId: StrictStr | None = None
    SupportedDPUSizes: list[StrictInt] | None = None
