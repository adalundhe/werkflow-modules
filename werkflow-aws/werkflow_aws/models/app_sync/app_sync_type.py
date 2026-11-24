from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncType(BaseModel):
    name: StrictStr | None = None
    description: StrictStr | None = None
    arn: StrictStr | None = None
    definition: StrictStr | None = None
    format: StrictStr | None = None
