from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .detective_timestamp_for_collection import DetectiveTimestampForCollection


class DetectiveMembershipDatasources(BaseModel):
    AccountId: StrictStr | None = None
    GraphArn: StrictStr | None = None
    DatasourcePackageIngestHistory: dict[StrictStr, dict[StrictStr, DetectiveTimestampForCollection]] | None = None
