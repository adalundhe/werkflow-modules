from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class APIGatewayGetTagsRequest(BaseModel):
    resourceArn: StrictStr
    position: StrictStr | None = None
    limit: StrictInt | None = None
