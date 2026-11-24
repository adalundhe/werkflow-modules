from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dashboard_gadget_position import DashboardGadgetPosition


class DashboardGadgetUpdateRequest(BaseModel):
    color: StrictStr | None = None
    position: DashboardGadgetPosition | None = None
    title: StrictStr | None = None
