from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .amplify_domain_association import AmplifyDomainAssociation


class AmplifyUpdateDomainAssociationResponse(BaseModel):
    domainAssociation: AmplifyDomainAssociation | None = None
    ResponseMetadata: dict[str, Any] | None = None
