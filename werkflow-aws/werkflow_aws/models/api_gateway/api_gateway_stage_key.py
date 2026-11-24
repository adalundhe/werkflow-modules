from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayStageKey(BaseModel):
    restApiId: StrictStr | None = None
    stageName: StrictStr | None = None
