from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DynamoDBExportSummary(BaseModel):
    ExportArn: StrictStr | None = None
    ExportStatus: StrictStr | None = None
    ExportType: StrictStr | None = None
