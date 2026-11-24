from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .rds_account_quota import RDSAccountQuota


class RDSDescribeAccountAttributesResponse(BaseModel):
    AccountQuotas: list[RDSAccountQuota] | None = None
    ResponseMetadata: dict[str, Any] | None = None
