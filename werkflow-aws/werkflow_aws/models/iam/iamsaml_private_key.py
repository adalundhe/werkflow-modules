from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class IAMSAMLPrivateKey(BaseModel):
    KeyId: StrictStr | None = None
    Timestamp: datetime.datetime | StrictStr | None = None
