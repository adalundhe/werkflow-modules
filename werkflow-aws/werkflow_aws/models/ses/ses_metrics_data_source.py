from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ses_export_metric import SESExportMetric


class SESMetricsDataSource(BaseModel):
    Dimensions: dict[StrictStr, list[StrictStr]] | None = None
    Namespace: StrictStr | None = None
    Metrics: list[SESExportMetric] | None = None
    StartDate: datetime.datetime | StrictStr | None = None
    EndDate: datetime.datetime | StrictStr | None = None
