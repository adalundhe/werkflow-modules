from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DMSEngineVersion(BaseModel):
    Version: StrictStr | None = None
    Lifecycle: StrictStr | None = None
    ReleaseStatus: StrictStr | None = None
    LaunchDate: datetime.datetime | StrictStr | None = None
    AutoUpgradeDate: datetime.datetime | StrictStr | None = None
    DeprecationDate: datetime.datetime | StrictStr | None = None
    ForceUpgradeDate: datetime.datetime | StrictStr | None = None
    AvailableUpgrades: list[StrictStr] | None = None
