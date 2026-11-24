from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectEvaluationFormQuestionAutomationAnswerSource(BaseModel):
    SourceType: StrictStr | None = None
