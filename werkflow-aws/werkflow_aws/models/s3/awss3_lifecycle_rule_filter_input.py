from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .awss3_lifecycle_rule_and_operator_input import AWSS3LifecycleRuleAndOperatorInput
from .awss3_tag import AWSS3Tag


class AWSS3LifecycleRuleFilterInput(BaseModel):
    Prefix: StrictStr | None = None
    Tag: AWSS3Tag | None = None
    ObjectSizeGreaterThan: StrictInt | None = None
    ObjectSizeLessThan: StrictInt | None = None
    And: AWSS3LifecycleRuleAndOperatorInput | None = None
