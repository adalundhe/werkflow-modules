from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ecs_daemon_capacity_provider import ECSDaemonCapacityProvider


class ECSDaemonRevisionDetail(BaseModel):
    arn: StrictStr | None = None
    capacityProviders: list[ECSDaemonCapacityProvider] | None = None
    totalRunningCount: StrictInt | None = None
    totalWithoutDaemonCount: StrictInt | None = None
