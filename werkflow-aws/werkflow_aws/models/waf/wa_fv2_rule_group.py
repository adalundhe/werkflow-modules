from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .wa_fv2_custom_response_body import WAFv2CustomResponseBody
from .wa_fv2_label_summary import WAFv2LabelSummary
from .wa_fv2_monetization_config import WAFv2MonetizationConfig
from .wa_fv2_rule import WAFv2Rule
from .wa_fv2_visibility_config import WAFv2VisibilityConfig


class WAFv2RuleGroup(BaseModel):
    Name: StrictStr | None = None
    Id: StrictStr | None = None
    Capacity: StrictInt | None = None
    ARN: StrictStr | None = None
    Description: StrictStr | None = None
    Rules: list[WAFv2Rule] | None = None
    VisibilityConfig: WAFv2VisibilityConfig | None = None
    LabelNamespace: StrictStr | None = None
    CustomResponseBodies: dict[StrictStr, WAFv2CustomResponseBody] | None = None
    AvailableLabels: list[WAFv2LabelSummary] | None = None
    ConsumedLabels: list[WAFv2LabelSummary] | None = None
    MonetizationConfig: WAFv2MonetizationConfig | None = None
