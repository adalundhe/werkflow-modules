from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFormationAnnotation(BaseModel):
    AnnotationName: StrictStr | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    RemediationMessage: StrictStr | None = None
    RemediationLink: StrictStr | None = None
    SeverityLevel: StrictStr | None = None
