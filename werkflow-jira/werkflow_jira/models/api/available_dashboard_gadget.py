from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AvailableDashboardGadget(BaseModel):
    moduleKey: StrictStr | None = None
    title: StrictStr | None = None
    uri: StrictStr | None = None
