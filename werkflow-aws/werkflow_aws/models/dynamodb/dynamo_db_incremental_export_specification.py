from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DynamoDBIncrementalExportSpecification(BaseModel):
    ExportFromTime: datetime.datetime | StrictStr | None = None
    ExportToTime: datetime.datetime | StrictStr | None = None
    ExportViewType: StrictStr | None = None
