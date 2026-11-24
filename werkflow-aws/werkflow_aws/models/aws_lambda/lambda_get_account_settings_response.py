from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lambda_account_limit import LambdaAccountLimit
from .lambda_account_usage import LambdaAccountUsage


class LambdaGetAccountSettingsResponse(BaseModel):
    AccountLimit: LambdaAccountLimit | None = None
    AccountUsage: LambdaAccountUsage | None = None
    ResponseMetadata: dict[str, Any] | None = None
