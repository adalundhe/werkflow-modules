from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .connect_evaluation_form_validation_finding import ConnectEvaluationFormValidationFinding


class ConnectGetEvaluationFormValidationResponse(BaseModel):
    Status: StrictStr | None = None
    FailureReason: StrictStr | None = None
    EvaluationFormId: StrictStr | None = None
    EvaluationFormVersion: StrictInt | None = None
    StartedTime: datetime.datetime | StrictStr | None = None
    Findings: list[ConnectEvaluationFormValidationFinding] | None = None
    ResponseMetadata: dict[str, Any] | None = None
