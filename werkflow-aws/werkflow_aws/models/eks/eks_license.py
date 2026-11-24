from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSLicense(BaseModel):
    id: StrictStr | None = None
    token: StrictStr | None = None
