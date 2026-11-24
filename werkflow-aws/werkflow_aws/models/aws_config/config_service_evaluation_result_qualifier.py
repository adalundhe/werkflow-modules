from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceEvaluationResultQualifier(BaseModel):
    ConfigRuleName: StrictStr | None = None
    ResourceType: StrictStr | None = None
    ResourceId: StrictStr | None = None
    EvaluationMode: StrictStr | None = None
