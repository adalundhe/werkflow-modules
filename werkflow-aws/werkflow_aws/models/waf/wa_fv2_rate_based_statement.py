from __future__ import annotations
from typing import TYPE_CHECKING
from pydantic import BaseModel, StrictInt, StrictStr
from .wa_fv2_forwarded_ip_config import WAFv2ForwardedIPConfig
from .wa_fv2_rate_based_statement_custom_key import WAFv2RateBasedStatementCustomKey

if TYPE_CHECKING:
    from .wa_fv2_statement import WAFv2Statement


class WAFv2RateBasedStatement(BaseModel):
    Limit: StrictInt | None = None
    EvaluationWindowSec: StrictInt | None = None
    AggregateKeyType: StrictStr | None = None
    ScopeDownStatement: WAFv2Statement | None = None
    ForwardedIPConfig: WAFv2ForwardedIPConfig | None = None
    CustomKeys: list[WAFv2RateBasedStatementCustomKey] | None = None
