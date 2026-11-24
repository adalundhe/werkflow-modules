from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class OpenSearchUpgradeStepItem(BaseModel):
    UpgradeStep: StrictStr | None = None
    UpgradeStepStatus: StrictStr | None = None
    Issues: list[StrictStr] | None = None
    ProgressPercent: StrictFloat | StrictInt | None = None
