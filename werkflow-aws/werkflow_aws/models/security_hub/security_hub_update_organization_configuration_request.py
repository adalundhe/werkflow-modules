from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool
from .security_hub_organization_configuration import SecurityHubOrganizationConfiguration


class SecurityHubUpdateOrganizationConfigurationRequest(BaseModel):
    AutoEnable: StrictBool
    AutoEnableStandards: Literal['NONE', 'DEFAULT'] | None = None
    OrganizationConfiguration: SecurityHubOrganizationConfiguration | None = None
