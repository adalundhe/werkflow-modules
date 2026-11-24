from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .managed_grafana_saml_configuration import ManagedGrafanaSamlConfiguration


class ManagedGrafanaSamlAuthentication(BaseModel):
    status: StrictStr | None = None
    configuration: ManagedGrafanaSamlConfiguration | None = None
