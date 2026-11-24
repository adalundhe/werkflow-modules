from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class QuickSightGetPolicyAssignmentResponse(BaseModel):
    PolicyArn: StrictStr | None = None
    PolicyName: StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    Revision: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
