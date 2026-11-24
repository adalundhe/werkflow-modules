from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsGetPolicyTemplateResponse(BaseModel):
    policyStoreId: StrictStr | None = None
    policyTemplateId: StrictStr | None = None
    description: StrictStr | None = None
    statement: StrictStr | None = None
    createdDate: datetime.datetime | StrictStr | None = None
    lastUpdatedDate: datetime.datetime | StrictStr | None = None
    name: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
