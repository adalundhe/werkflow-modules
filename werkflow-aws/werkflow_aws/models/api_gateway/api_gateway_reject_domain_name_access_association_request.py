from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayRejectDomainNameAccessAssociationRequest(BaseModel):
    domainNameAccessAssociationArn: StrictStr
    domainNameArn: StrictStr
