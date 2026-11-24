from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CodePipelineActionTypeProperty(BaseModel):
    name: StrictStr | None = None
    optional: StrictBool | None = None
    key: StrictBool | None = None
    noEcho: StrictBool | None = None
    queryable: StrictBool | None = None
    description: StrictStr | None = None
