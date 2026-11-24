from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .connect_evaluation_form_ai_version_lifecycle import ConnectEvaluationFormAIVersionLifecycle


class ConnectEvaluationFormAIVersionSummary(BaseModel):
    AIVersionName: StrictStr | None = None
    AIVersionLifecycle: ConnectEvaluationFormAIVersionLifecycle | None = None
