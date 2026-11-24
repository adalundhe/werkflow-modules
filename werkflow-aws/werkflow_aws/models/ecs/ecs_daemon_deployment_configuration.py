from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt
from .ecs_daemon_alarm_configuration import ECSDaemonAlarmConfiguration


class ECSDaemonDeploymentConfiguration(BaseModel):
    drainPercent: StrictFloat | StrictInt | None = None
    alarms: ECSDaemonAlarmConfiguration | None = None
    bakeTimeInMinutes: StrictInt | None = None
