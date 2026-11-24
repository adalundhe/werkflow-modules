from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsUpdateIdentitySourceResponse(BaseModel):
    createdDate: datetime.datetime | StrictStr | None = None
    identitySourceId: StrictStr | None = None
    lastUpdatedDate: datetime.datetime | StrictStr | None = None
    policyStoreId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
