from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSLimitation(BaseModel):
    DatabaseId: StrictStr | None = None
    EngineName: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Impact: StrictStr | None = None
    Type: StrictStr | None = None
