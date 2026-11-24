from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .amplify_domain_association import AmplifyDomainAssociation


class AmplifyListDomainAssociationsResponse(BaseModel):
    domainAssociations: list[AmplifyDomainAssociation] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
