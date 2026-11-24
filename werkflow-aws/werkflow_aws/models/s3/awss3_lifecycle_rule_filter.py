from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .awss3_lifecycle_rule_and_operator import AWSS3LifecycleRuleAndOperator
from .awss3_tag_output import AWSS3TagOutput


class AWSS3LifecycleRuleFilter(BaseModel):
    Prefix: StrictStr | None = None
    Tag: AWSS3TagOutput | None = None
    ObjectSizeGreaterThan: StrictInt | None = None
    ObjectSizeLessThan: StrictInt | None = None
    And: AWSS3LifecycleRuleAndOperator | None = None
