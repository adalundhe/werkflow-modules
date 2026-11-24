from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OrganizationsEffectivePolicyValidationError(BaseModel):
    ErrorCode: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    PathToError: StrictStr | None = None
    ContributingPolicies: list[StrictStr] | None = None
