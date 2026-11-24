from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class APIGatewayGetDomainNamesRequest(BaseModel):
    position: StrictStr | None = None
    limit: StrictInt | None = None
    resourceOwner: Literal['SELF', 'OTHER_ACCOUNTS'] | None = None
