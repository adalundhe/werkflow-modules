from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .data_zone_data_source_error_message import DataZoneDataSourceErrorMessage
from .data_zone_lineage_info import DataZoneLineageInfo


class DataZoneDataSourceRunActivity(BaseModel):
    database: StrictStr | None = None
    dataSourceRunId: StrictStr | None = None
    technicalName: StrictStr | None = None
    dataAssetStatus: StrictStr | None = None
    projectId: StrictStr | None = None
    dataAssetId: StrictStr | None = None
    technicalDescription: StrictStr | None = None
    errorMessage: DataZoneDataSourceErrorMessage | None = None
    lineageSummary: DataZoneLineageInfo | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
