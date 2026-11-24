from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class APIGatewayCreateDomainNameAccessAssociationResponse(BaseModel):
    domainNameAccessAssociationArn: StrictStr | None = None
    domainNameArn: StrictStr | None = None
    accessAssociationSourceType: StrictStr | None = None
    accessAssociationSource: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
