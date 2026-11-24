from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KMSXksKeyConfigurationType(BaseModel):
    Id: StrictStr | None = None
