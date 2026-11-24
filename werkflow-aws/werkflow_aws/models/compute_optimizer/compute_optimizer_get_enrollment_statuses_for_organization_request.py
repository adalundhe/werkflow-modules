from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .compute_optimizer_enrollment_filter import ComputeOptimizerEnrollmentFilter


class ComputeOptimizerGetEnrollmentStatusesForOrganizationRequest(BaseModel):
    filters: list[ComputeOptimizerEnrollmentFilter] | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
