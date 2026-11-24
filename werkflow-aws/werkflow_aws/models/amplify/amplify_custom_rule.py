from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AmplifyCustomRule(BaseModel):
    source: StrictStr | None = None
    target: StrictStr | None = None
    status: StrictStr | None = None
    condition: StrictStr | None = None
