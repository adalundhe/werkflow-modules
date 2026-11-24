from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ConnectContactAnalysisReference(BaseModel):
    Name: StrictStr | None = None
    Value: StrictStr | None = None
    Status: StrictStr | None = None
    Arn: StrictStr | None = None
    AnalyticsMode: StrictStr | None = None
    IsRedacted: StrictBool | None = None
