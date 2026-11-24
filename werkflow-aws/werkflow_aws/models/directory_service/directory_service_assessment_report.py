from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .directory_service_assessment_validation import DirectoryServiceAssessmentValidation


class DirectoryServiceAssessmentReport(BaseModel):
    DomainControllerIp: StrictStr | None = None
    Validations: list[DirectoryServiceAssessmentValidation] | None = None
