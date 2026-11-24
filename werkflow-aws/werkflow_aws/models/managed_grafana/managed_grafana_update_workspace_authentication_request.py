from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .managed_grafana_saml_configuration import ManagedGrafanaSamlConfiguration


class ManagedGrafanaUpdateWorkspaceAuthenticationRequest(BaseModel):
    workspaceId: StrictStr
    authenticationProviders: list[Literal['AWS_SSO', 'SAML']]
    samlConfiguration: ManagedGrafanaSamlConfiguration | None = None
