from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class APIGatewayGetApiKeysRequest(BaseModel):
    position: StrictStr | None = None
    limit: StrictInt | None = None
    nameQuery: StrictStr | None = None
    customerId: StrictStr | None = None
    includeValues: StrictBool | None = None
