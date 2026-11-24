from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchEksSeccompProfile(BaseModel):
    type: StrictStr | None = None
    localhostProfile: StrictStr | None = None
