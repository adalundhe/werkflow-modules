from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSProvider(BaseModel):
    keyArn: StrictStr | None = None
