from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ApprovalConfigurationPreview(BaseModel):
    active: StrictStr | None = None
    transitionApproved: StrictStr | None = None
    transitionRejected: StrictStr | None = None
