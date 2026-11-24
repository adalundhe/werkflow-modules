from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .managed_grafana_aws_sso_authentication import ManagedGrafanaAwsSsoAuthentication
from .managed_grafana_saml_authentication import ManagedGrafanaSamlAuthentication


class ManagedGrafanaAuthenticationDescription(BaseModel):
    providers: list[StrictStr] | None = None
    saml: ManagedGrafanaSamlAuthentication | None = None
    awsSso: ManagedGrafanaAwsSsoAuthentication | None = None
