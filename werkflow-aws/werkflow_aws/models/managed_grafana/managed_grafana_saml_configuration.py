from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .managed_grafana_assertion_attributes import ManagedGrafanaAssertionAttributes
from .managed_grafana_idp_metadata import ManagedGrafanaIdpMetadata
from .managed_grafana_role_values import ManagedGrafanaRoleValues


class ManagedGrafanaSamlConfiguration(BaseModel):
    idpMetadata: ManagedGrafanaIdpMetadata | None = None
    assertionAttributes: ManagedGrafanaAssertionAttributes | None = None
    roleValues: ManagedGrafanaRoleValues | None = None
    allowedOrganizations: list[StrictStr] | None = None
    loginValidityDuration: StrictInt | None = None
