from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .dev_ops_guru_log_anomaly_showcase import DevOpsGuruLogAnomalyShowcase


class DevOpsGuruAnomalousLogGroup(BaseModel):
    LogGroupName: StrictStr | None = None
    ImpactStartTime: datetime.datetime | StrictStr | None = None
    ImpactEndTime: datetime.datetime | StrictStr | None = None
    NumberOfLogLinesScanned: StrictInt | None = None
    LogAnomalyShowcases: list[DevOpsGuruLogAnomalyShowcase] | None = None
