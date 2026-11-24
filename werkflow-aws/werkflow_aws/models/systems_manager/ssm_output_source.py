from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMOutputSource(BaseModel):
    OutputSourceId: StrictStr | None = None
    OutputSourceType: StrictStr | None = None
