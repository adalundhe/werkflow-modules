from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class KinesisAnalyticsMonitoringConfigurationUpdate(BaseModel):
    ConfigurationTypeUpdate: Literal['DEFAULT', 'CUSTOM'] | None = None
    MetricsLevelUpdate: Literal['APPLICATION', 'TASK', 'OPERATOR', 'PARALLELISM'] | None = None
    LogLevelUpdate: Literal['INFO', 'WARN', 'ERROR', 'DEBUG'] | None = None
