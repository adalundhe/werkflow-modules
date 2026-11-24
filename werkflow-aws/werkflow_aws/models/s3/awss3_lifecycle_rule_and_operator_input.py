from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .awss3_tag import AWSS3Tag


class AWSS3LifecycleRuleAndOperatorInput(BaseModel):
    Prefix: StrictStr | None = None
    Tags: list[AWSS3Tag] | None = None
    ObjectSizeGreaterThan: StrictInt | None = None
    ObjectSizeLessThan: StrictInt | None = None
