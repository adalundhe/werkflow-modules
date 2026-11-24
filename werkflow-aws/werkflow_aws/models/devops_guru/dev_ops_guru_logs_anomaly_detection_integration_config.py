from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class DevOpsGuruLogsAnomalyDetectionIntegrationConfig(BaseModel):
    OptInStatus: Literal['ENABLED', 'DISABLED'] | None = None
