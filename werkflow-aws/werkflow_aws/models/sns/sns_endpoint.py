from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SNSEndpoint(BaseModel):
    EndpointArn: StrictStr | None = None
    Attributes: dict[StrictStr, StrictStr] | None = None
