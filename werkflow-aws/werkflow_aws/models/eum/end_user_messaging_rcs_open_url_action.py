from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingRcsOpenUrlAction(BaseModel):
    Text: StrictStr
    PostbackData: StrictStr
    Url: StrictStr
    Application: StrictStr | None = None
    WebviewViewMode: StrictStr | None = None
