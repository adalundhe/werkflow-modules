from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class KinesisAnalyticsZeppelinMonitoringConfiguration(BaseModel):
    LogLevel: Literal['INFO', 'WARN', 'ERROR', 'DEBUG']
