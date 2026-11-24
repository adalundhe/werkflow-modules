from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SNSSetEndpointAttributesRequest(BaseModel):
    EndpointArn: StrictStr
    Attributes: dict[StrictStr, StrictStr]
