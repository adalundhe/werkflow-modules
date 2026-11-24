from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .access_analyzer_kms_grant_constraints import AccessAnalyzerKmsGrantConstraints


class AccessAnalyzerKmsGrantConfiguration(BaseModel):
    operations: list[StrictStr] | None = None
    granteePrincipal: StrictStr | None = None
    retiringPrincipal: StrictStr | None = None
    constraints: AccessAnalyzerKmsGrantConstraints | None = None
    issuingAccount: StrictStr | None = None
