from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class GluePutResourcePolicyRequest(BaseModel):
    PolicyInJson: StrictStr
    ResourceArn: StrictStr | None = None
    PolicyHashCondition: StrictStr | None = None
    PolicyExistsCondition: Literal['MUST_EXIST', 'NOT_EXIST', 'NONE'] | None = None
    EnableHybrid: Literal['TRUE', 'FALSE'] | None = None
