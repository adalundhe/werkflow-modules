from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CodePipelineRuleConfigurationProperty(BaseModel):
    name: StrictStr | None = None
    required: StrictBool | None = None
    key: StrictBool | None = None
    secret: StrictBool | None = None
    queryable: StrictBool | None = None
    description: StrictStr | None = None
    type: StrictStr | None = None
