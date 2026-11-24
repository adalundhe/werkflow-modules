from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowIncrementalPullConfig(BaseModel):
    datetimeTypeFieldName: StrictStr | None = None
