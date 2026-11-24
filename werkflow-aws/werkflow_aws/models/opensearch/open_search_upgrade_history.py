from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .open_search_upgrade_step_item import OpenSearchUpgradeStepItem


class OpenSearchUpgradeHistory(BaseModel):
    UpgradeName: StrictStr | None = None
    StartTimestamp: datetime.datetime | StrictStr | None = None
    UpgradeStatus: StrictStr | None = None
    StepsList: list[OpenSearchUpgradeStepItem] | None = None
