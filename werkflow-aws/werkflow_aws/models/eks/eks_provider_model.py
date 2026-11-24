from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSProviderModel(BaseModel):
    keyArn: StrictStr | None = None
