from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dms_error_details import DMSErrorDetails
from .dms_export_sql_details import DMSExportSqlDetails
from .dms_progress import DMSProgress


class DMSSchemaConversionRequest(BaseModel):
    Status: StrictStr | None = None
    RequestIdentifier: StrictStr | None = None
    MigrationProjectArn: StrictStr | None = None
    Error: DMSErrorDetails | None = None
    ExportSqlDetails: DMSExportSqlDetails | None = None
    Progress: DMSProgress | None = None
