from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class AccessAnalyzerUpdateFindingsRequest(BaseModel):
    analyzerArn: StrictStr
    status: Literal['ACTIVE', 'ARCHIVED']
    ids: list[StrictStr] | None = None
    resourceArn: StrictStr | None = None
    clientToken: StrictStr | None = None
