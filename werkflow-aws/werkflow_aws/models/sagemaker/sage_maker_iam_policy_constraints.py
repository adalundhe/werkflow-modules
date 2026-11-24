from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerIamPolicyConstraints(BaseModel):
    SourceIp: StrictStr | None = None
    VpcSourceIp: StrictStr | None = None
