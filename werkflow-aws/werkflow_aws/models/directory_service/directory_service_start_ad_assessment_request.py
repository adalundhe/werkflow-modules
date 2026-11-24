from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .directory_service_assessment_configuration import DirectoryServiceAssessmentConfiguration


class DirectoryServiceStartADAssessmentRequest(BaseModel):
    AssessmentConfiguration: DirectoryServiceAssessmentConfiguration | None = None
    DirectoryId: StrictStr | None = None
