from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class KinesisAnalyticsMonitoringConfiguration(BaseModel):
    ConfigurationType: Literal['DEFAULT', 'CUSTOM']
    MetricsLevel: Literal['APPLICATION', 'TASK', 'OPERATOR', 'PARALLELISM'] | None = None
    LogLevel: Literal['INFO', 'WARN', 'ERROR', 'DEBUG'] | None = None
