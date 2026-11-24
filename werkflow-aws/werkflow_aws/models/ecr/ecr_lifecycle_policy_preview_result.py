from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .ecr_lifecycle_policy_rule_action import ECRLifecyclePolicyRuleAction


class ECRLifecyclePolicyPreviewResult(BaseModel):
    imageTags: list[StrictStr] | None = None
    imageDigest: StrictStr | None = None
    imagePushedAt: datetime.datetime | StrictStr | None = None
    action: ECRLifecyclePolicyRuleAction | None = None
    appliedRulePriority: StrictInt | None = None
    storageClass: StrictStr | None = None
