from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightRdsParameters(BaseModel):
    InstanceId: StrictStr | None = None
    Database: StrictStr | None = None
