from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesAccountLink(BaseModel):
    AccountLinkId: StrictStr | None = None
    AccountLinkStatus: StrictStr | None = None
    SourceAccountId: StrictStr | None = None
    TargetAccountId: StrictStr | None = None
