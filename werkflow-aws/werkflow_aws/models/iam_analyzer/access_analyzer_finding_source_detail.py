from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AccessAnalyzerFindingSourceDetail(BaseModel):
    accessPointArn: StrictStr | None = None
    accessPointAccount: StrictStr | None = None
