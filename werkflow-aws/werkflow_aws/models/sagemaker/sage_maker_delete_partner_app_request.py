from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerDeletePartnerAppRequest(BaseModel):
    Arn: StrictStr
    ClientToken: StrictStr | None = None
