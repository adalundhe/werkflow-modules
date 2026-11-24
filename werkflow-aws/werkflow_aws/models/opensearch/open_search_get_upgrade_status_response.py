from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class OpenSearchGetUpgradeStatusResponse(BaseModel):
    UpgradeStep: StrictStr | None = None
    StepStatus: StrictStr | None = None
    UpgradeName: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
