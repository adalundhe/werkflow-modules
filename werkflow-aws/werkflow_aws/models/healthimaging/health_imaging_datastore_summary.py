from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class HealthImagingDatastoreSummary(BaseModel):
    datastoreId: StrictStr | None = None
    datastoreName: StrictStr | None = None
    datastoreStatus: StrictStr | None = None
    datastoreArn: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
