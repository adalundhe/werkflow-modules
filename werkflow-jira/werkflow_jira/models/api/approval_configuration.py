from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ApprovalConfiguration(BaseModel):
    active: StrictStr | None = None
    conditionType: StrictStr | None = None
    conditionValue: StrictStr | None = None
    exclude: list[StrictStr] | None = None
    fieldId: StrictStr | None = None
    prePopulatedFieldId: StrictStr | None = None
    transitionApproved: StrictStr | None = None
    transitionRejected: StrictStr | None = None
