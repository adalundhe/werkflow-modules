from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .organizations_enabled_service_principal import OrganizationsEnabledServicePrincipal


class OrganizationsListAWSServiceAccessForOrganizationResponse(BaseModel):
    EnabledServicePrincipals: list[OrganizationsEnabledServicePrincipal] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
