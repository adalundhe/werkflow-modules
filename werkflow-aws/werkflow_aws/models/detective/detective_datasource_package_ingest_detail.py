from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .detective_timestamp_for_collection import DetectiveTimestampForCollection


class DetectiveDatasourcePackageIngestDetail(BaseModel):
    DatasourcePackageIngestState: StrictStr | None = None
    LastIngestStateChange: dict[StrictStr, DetectiveTimestampForCollection] | None = None
