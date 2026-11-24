from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayDeleteDomainNameAccessAssociationRequest(BaseModel):
    domainNameAccessAssociationArn: StrictStr
