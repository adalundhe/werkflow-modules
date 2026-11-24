from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .msk_logging_info_model import MSKLoggingInfoModel
from .msk_open_monitoring_info import MSKOpenMonitoringInfo


class MSKUpdateMonitoringRequest(BaseModel):
    ClusterArn: StrictStr
    CurrentVersion: StrictStr
    EnhancedMonitoring: Literal['DEFAULT', 'PER_BROKER', 'PER_TOPIC_PER_BROKER', 'PER_TOPIC_PER_PARTITION'] | None = None
    OpenMonitoring: MSKOpenMonitoringInfo | None = None
    LoggingInfo: MSKLoggingInfoModel | None = None
