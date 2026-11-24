from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .msk_assessment_parameters import MSKAssessmentParameters


class MSKCreateAssessmentRequest(BaseModel):
    AssessmentType: Literal['UPDATE_BROKER_TYPE']
    ClusterArn: StrictStr
    AssessmentParameters: MSKAssessmentParameters | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
