from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr


class MSKCreateAssessmentResponse(BaseModel):
    AssessmentArn: StrictStr | None = None
    AssessmentType: StrictStr | None = None
    ClusterArn: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
