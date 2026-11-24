from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class AuditManagerValidateAssessmentReportIntegrityResponse(BaseModel):
    signatureValid: StrictBool | None = None
    signatureAlgorithm: StrictStr | None = None
    signatureDateTime: StrictStr | None = None
    signatureKeyId: StrictStr | None = None
    validationErrors: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
