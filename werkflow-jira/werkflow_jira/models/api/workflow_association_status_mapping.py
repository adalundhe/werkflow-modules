from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkflowAssociationStatusMapping(BaseModel):
    newStatusId: StrictStr | None = None
    oldStatusId: StrictStr | None = None
