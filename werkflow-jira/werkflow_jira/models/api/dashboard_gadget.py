from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .dashboard_gadget_position import DashboardGadgetPosition


class DashboardGadget(BaseModel):
    color: StrictStr | None = None
    id: StrictInt | None = None
    moduleKey: StrictStr | None = None
    position: DashboardGadgetPosition | None = None
    title: StrictStr | None = None
    uri: StrictStr | None = None
