from __future__ import annotations
from pydantic import BaseModel, StrictStr


class APIGatewayDomainNameAccessAssociation(BaseModel):
    domainNameAccessAssociationArn: StrictStr | None = None
    domainNameArn: StrictStr | None = None
    accessAssociationSourceType: StrictStr | None = None
    accessAssociationSource: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
