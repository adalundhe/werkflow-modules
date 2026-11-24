from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightTopicRefreshDetails(BaseModel):
    RefreshArn: StrictStr | None = None
    RefreshId: StrictStr | None = None
    RefreshStatus: StrictStr | None = None
