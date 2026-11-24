from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_export_destination import SecurityHubExportDestination
from .security_hub_export_output import SecurityHubExportOutput
from .security_hub_export_scopes import SecurityHubExportScopes


class SecurityHubStartExportJobV2Request(BaseModel):
    Destination: SecurityHubExportDestination
    OutputConfiguration: SecurityHubExportOutput
    Name: StrictStr | None = None
    Scopes: SecurityHubExportScopes | None = None
    ClientToken: StrictStr | None = None
