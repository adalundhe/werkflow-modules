from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class UiModificationContextDetails(BaseModel):
    id: StrictStr | None = None
    isAvailable: StrictBool | None = None
    issueTypeId: StrictStr | None = None
    portalId: StrictStr | None = None
    projectId: StrictStr | None = None
    requestTypeId: StrictStr | None = None
    viewType: StrictStr | None = None
