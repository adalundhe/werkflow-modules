from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class KinesisAnalyticsZeppelinMonitoringConfigurationUpdate(BaseModel):
    LogLevelUpdate: Literal['INFO', 'WARN', 'ERROR', 'DEBUG']
