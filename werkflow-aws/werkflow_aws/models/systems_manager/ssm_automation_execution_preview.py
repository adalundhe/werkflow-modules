from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ssm_target_preview import SSMTargetPreview


class SSMAutomationExecutionPreview(BaseModel):
    StepPreviews: dict[StrictStr, StrictInt] | None = None
    Regions: list[StrictStr] | None = None
    TargetPreviews: list[SSMTargetPreview] | None = None
    TotalAccounts: StrictInt | None = None
