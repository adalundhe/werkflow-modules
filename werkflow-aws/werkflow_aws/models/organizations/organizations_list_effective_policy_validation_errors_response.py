from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .organizations_effective_policy_validation_error import OrganizationsEffectivePolicyValidationError


class OrganizationsListEffectivePolicyValidationErrorsResponse(BaseModel):
    AccountId: StrictStr | None = None
    PolicyType: StrictStr | None = None
    Path: StrictStr | None = None
    EvaluationTimestamp: datetime.datetime | StrictStr | None = None
    NextToken: StrictStr | None = None
    EffectivePolicyValidationErrors: list[OrganizationsEffectivePolicyValidationError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
