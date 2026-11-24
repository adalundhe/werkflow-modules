from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .data_zone_data_source_error_message import DataZoneDataSourceErrorMessage
from .data_zone_data_source_run_lineage_summary import DataZoneDataSourceRunLineageSummary
from .data_zone_run_statistics_for_assets import DataZoneRunStatisticsForAssets


class DataZoneDataSourceRunSummary(BaseModel):
    id: StrictStr | None = None
    dataSourceId: StrictStr | None = None
    type: StrictStr | None = None
    status: StrictStr | None = None
    projectId: StrictStr | None = None
    runStatisticsForAssets: DataZoneRunStatisticsForAssets | None = None
    errorMessage: DataZoneDataSourceErrorMessage | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
    startedAt: datetime.datetime | StrictStr | None = None
    stoppedAt: datetime.datetime | StrictStr | None = None
    lineageSummary: DataZoneDataSourceRunLineageSummary | None = None
