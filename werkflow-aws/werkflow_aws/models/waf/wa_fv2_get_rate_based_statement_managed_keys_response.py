from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .wa_fv2_rate_based_statement_managed_keys_ip_set import WAFv2RateBasedStatementManagedKeysIPSet


class WAFv2GetRateBasedStatementManagedKeysResponse(BaseModel):
    ManagedKeysIPV4: WAFv2RateBasedStatementManagedKeysIPSet | None = None
    ManagedKeysIPV6: WAFv2RateBasedStatementManagedKeysIPSet | None = None
    ResponseMetadata: dict[str, Any] | None = None
