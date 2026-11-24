from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .security_hub_export_destination import SecurityHubExportDestination
from .security_hub_export_output import SecurityHubExportOutput
from .security_hub_export_scopes import SecurityHubExportScopes


class SecurityHubGetExportJobV2Response(BaseModel):
    ExportJobId: StrictStr | None = None
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    DataType: StrictStr | None = None
    OutputConfiguration: SecurityHubExportOutput | None = None
    Scopes: SecurityHubExportScopes | None = None
    Destination: SecurityHubExportDestination | None = None
    FailureCode: StrictStr | None = None
    FailureMessage: StrictStr | None = None
    StartedAt: datetime.datetime | StrictStr | None = None
    EndedAt: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
