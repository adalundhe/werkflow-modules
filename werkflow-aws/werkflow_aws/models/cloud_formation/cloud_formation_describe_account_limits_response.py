from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_formation_account_limit import CloudFormationAccountLimit


class CloudFormationDescribeAccountLimitsResponse(BaseModel):
    AccountLimits: list[CloudFormationAccountLimit] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
