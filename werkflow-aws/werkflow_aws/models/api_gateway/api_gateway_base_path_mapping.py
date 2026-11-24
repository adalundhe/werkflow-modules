from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayBasePathMapping(BaseModel):
    basePath: StrictStr | None = None
    restApiId: StrictStr | None = None
    stage: StrictStr | None = None
