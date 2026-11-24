from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class KendraClickFeedback(BaseModel):
    ResultId: StrictStr
    ClickTime: datetime.datetime | StrictStr
