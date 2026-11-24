from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTAuthorizerSummary(BaseModel):
    authorizerName: StrictStr | None = None
    authorizerArn: StrictStr | None = None
