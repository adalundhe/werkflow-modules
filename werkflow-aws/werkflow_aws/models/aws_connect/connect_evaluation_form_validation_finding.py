from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_evaluation_form_validation_finding_item import ConnectEvaluationFormValidationFindingItem


class ConnectEvaluationFormValidationFinding(BaseModel):
    IssueCode: StrictStr | None = None
    Items: list[ConnectEvaluationFormValidationFindingItem] | None = None
    Description: StrictStr | None = None
    Suggestion: StrictStr | None = None
    Severity: StrictStr | None = None
