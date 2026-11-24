from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .wa_fv2_managed_rule_set_version import WAFv2ManagedRuleSetVersion


class WAFv2ManagedRuleSet(BaseModel):
    Name: StrictStr | None = None
    Id: StrictStr | None = None
    ARN: StrictStr | None = None
    Description: StrictStr | None = None
    PublishedVersions: dict[StrictStr, WAFv2ManagedRuleSetVersion] | None = None
    RecommendedVersion: StrictStr | None = None
    LabelNamespace: StrictStr | None = None
