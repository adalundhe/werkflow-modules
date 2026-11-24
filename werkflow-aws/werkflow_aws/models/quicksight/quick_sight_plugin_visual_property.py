from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightPluginVisualProperty(BaseModel):
    Name: StrictStr | None = None
    Value: StrictStr | None = None
