from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ssm_validation_finding_scope import SSMValidationFindingScope


class SSMValidationFinding(BaseModel):
    Type: StrictStr | None = None
    Code: StrictStr | None = None
    Message: StrictStr | None = None
    ProviderMessage: StrictStr | None = None
    Scope: SSMValidationFindingScope | None = None
