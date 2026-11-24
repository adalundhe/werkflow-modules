from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppFlowMarketoSourceProperties(BaseModel):
    object: StrictStr | None = None
