from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsCreatePolicyStoreAliasResponse(BaseModel):
    aliasName: StrictStr | None = None
    policyStoreId: StrictStr | None = None
    aliasArn: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
