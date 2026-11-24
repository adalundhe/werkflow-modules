from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class APIGatewayCreateDomainNameAccessAssociationRequest(BaseModel):
    domainNameArn: StrictStr
    accessAssociationSourceType: Literal['VPCE']
    accessAssociationSource: StrictStr
    tags: dict[StrictStr, StrictStr] | None = None
