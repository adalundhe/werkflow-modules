from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ecs_instance_health_check_result import ECSInstanceHealthCheckResult


class ECSContainerInstanceHealthStatus(BaseModel):
    overallStatus: StrictStr | None = None
    details: list[ECSInstanceHealthCheckResult] | None = None
