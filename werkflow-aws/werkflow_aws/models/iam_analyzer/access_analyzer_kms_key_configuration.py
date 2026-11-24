from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .access_analyzer_kms_grant_configuration import AccessAnalyzerKmsGrantConfiguration


class AccessAnalyzerKmsKeyConfiguration(BaseModel):
    keyPolicies: dict[StrictStr, StrictStr] | None = None
    grants: list[AccessAnalyzerKmsGrantConfiguration] | None = None
