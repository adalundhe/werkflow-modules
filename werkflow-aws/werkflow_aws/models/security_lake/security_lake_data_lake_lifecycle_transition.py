from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityLakeDataLakeLifecycleTransition(BaseModel):
    days: StrictInt | None = None
    storageClass: StrictStr | None = None
