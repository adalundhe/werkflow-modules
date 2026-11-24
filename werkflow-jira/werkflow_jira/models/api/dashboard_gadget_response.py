from __future__ import annotations
from pydantic import BaseModel
from .dashboard_gadget import DashboardGadget


class DashboardGadgetResponse(BaseModel):
    gadgets: list[DashboardGadget] | None = None
