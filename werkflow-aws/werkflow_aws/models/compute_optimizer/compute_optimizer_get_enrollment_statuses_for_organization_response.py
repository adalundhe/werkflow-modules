from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .compute_optimizer_account_enrollment_status import ComputeOptimizerAccountEnrollmentStatus


class ComputeOptimizerGetEnrollmentStatusesForOrganizationResponse(BaseModel):
    accountEnrollmentStatuses: list[ComputeOptimizerAccountEnrollmentStatus] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
