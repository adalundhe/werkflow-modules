from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .wa_fv2_label_summary import WAFv2LabelSummary
from .wa_fv2_rule_summary import WAFv2RuleSummary


class WAFv2DescribeManagedRuleGroupResponse(BaseModel):
    VersionName: StrictStr | None = None
    SnsTopicArn: StrictStr | None = None
    Capacity: StrictInt | None = None
    Rules: list[WAFv2RuleSummary] | None = None
    LabelNamespace: StrictStr | None = None
    AvailableLabels: list[WAFv2LabelSummary] | None = None
    ConsumedLabels: list[WAFv2LabelSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
