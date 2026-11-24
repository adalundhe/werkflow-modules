from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .iam_position import IAMPosition


class IAMStatement(BaseModel):
    SourcePolicyId: StrictStr | None = None
    SourcePolicyType: StrictStr | None = None
    StartPosition: IAMPosition | None = None
    EndPosition: IAMPosition | None = None
