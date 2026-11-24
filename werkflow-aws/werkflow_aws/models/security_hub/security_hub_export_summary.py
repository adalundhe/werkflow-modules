from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .security_hub_export_destination import SecurityHubExportDestination
from .security_hub_export_output_summary import SecurityHubExportOutputSummary
from .security_hub_export_scopes import SecurityHubExportScopes


class SecurityHubExportSummary(BaseModel):
    ExportJobId: StrictStr | None = None
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    DataType: StrictStr | None = None
    OutputConfiguration: SecurityHubExportOutputSummary | None = None
    Scopes: SecurityHubExportScopes | None = None
    Destination: SecurityHubExportDestination | None = None
    FailureCode: StrictStr | None = None
    FailureMessage: StrictStr | None = None
    StartedAt: datetime.datetime | StrictStr | None = None
    EndedAt: datetime.datetime | StrictStr | None = None
