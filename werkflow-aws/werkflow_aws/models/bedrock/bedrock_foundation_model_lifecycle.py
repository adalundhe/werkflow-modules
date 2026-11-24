from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class BedrockFoundationModelLifecycle(BaseModel):
    status: StrictStr | None = None
    startOfLifeTime: datetime.datetime | StrictStr | None = None
    endOfLifeTime: datetime.datetime | StrictStr | None = None
    legacyTime: datetime.datetime | StrictStr | None = None
    publicExtendedAccessTime: datetime.datetime | StrictStr | None = None
