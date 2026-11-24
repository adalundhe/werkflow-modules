from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectWidgetDestination(BaseModel):
    WidgetId: StrictStr
    ProfileId: StrictStr
