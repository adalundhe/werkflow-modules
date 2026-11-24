from __future__ import annotations
from pydantic import BaseModel
from .available_dashboard_gadget import AvailableDashboardGadget


class AvailableDashboardGadgetsResponse(BaseModel):
    gadgets: list[AvailableDashboardGadget] | None = None
