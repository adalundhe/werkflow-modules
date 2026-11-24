from __future__ import annotations
from pydantic import BaseModel
from .security_hub_s3_export_destination import SecurityHubS3ExportDestination


class SecurityHubExportDestination(BaseModel):
    S3: SecurityHubS3ExportDestination | None = None
