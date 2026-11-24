from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .awss3_tag_output import AWSS3TagOutput


class AWSS3LifecycleRuleAndOperator(BaseModel):
    Prefix: StrictStr | None = None
    Tags: list[AWSS3TagOutput] | None = None
    ObjectSizeGreaterThan: StrictInt | None = None
    ObjectSizeLessThan: StrictInt | None = None
