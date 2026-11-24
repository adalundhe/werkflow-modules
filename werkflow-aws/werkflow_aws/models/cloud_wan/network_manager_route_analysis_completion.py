from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NetworkManagerRouteAnalysisCompletion(BaseModel):
    ResultCode: StrictStr | None = None
    ReasonCode: StrictStr | None = None
    ReasonContext: dict[StrictStr, StrictStr] | None = None
