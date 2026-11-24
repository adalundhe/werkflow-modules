from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightUserIdentifier(BaseModel):
    UserName: StrictStr | None = None
    Email: StrictStr | None = None
    UserArn: StrictStr | None = None
