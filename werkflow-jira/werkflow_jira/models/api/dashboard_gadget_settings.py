from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .dashboard_gadget_position import DashboardGadgetPosition


class DashboardGadgetSettings(BaseModel):
    color: StrictStr | None = None
    ignoreUriAndModuleKeyValidation: StrictBool | None = None
    moduleKey: StrictStr | None = None
    position: DashboardGadgetPosition | None = None
    title: StrictStr | None = None
    uri: StrictStr | None = None
