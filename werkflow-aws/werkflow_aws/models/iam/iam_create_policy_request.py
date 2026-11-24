from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .iam_tag import IAMTag


class IAMCreatePolicyRequest(BaseModel):
    PolicyName: StrictStr
    PolicyDocument: StrictStr
    Path: StrictStr | None = None
    Description: StrictStr | None = None
    Tags: list[IAMTag] | None = None
