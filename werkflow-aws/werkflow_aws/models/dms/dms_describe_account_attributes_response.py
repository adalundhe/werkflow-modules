from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_account_quota import DMSAccountQuota


class DMSDescribeAccountAttributesResponse(BaseModel):
    AccountQuotas: list[DMSAccountQuota] | None = None
    UniqueAccountIdentifier: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
