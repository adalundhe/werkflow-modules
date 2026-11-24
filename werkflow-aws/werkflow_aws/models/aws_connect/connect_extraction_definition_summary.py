from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConnectExtractionDefinitionSummary(BaseModel):
    Name: StrictStr | None = None
    ExtractionDefinitionId: StrictStr | None = None
    ExtractionDefinitionArn: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedBy: StrictStr | None = None
