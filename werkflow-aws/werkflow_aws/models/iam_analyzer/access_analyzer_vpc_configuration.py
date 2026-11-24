from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AccessAnalyzerVpcConfiguration(BaseModel):
    vpcId: StrictStr | None = None
