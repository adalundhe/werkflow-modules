from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectEvaluationFormLanguageConfiguration(BaseModel):
    FormLanguage: StrictStr | None = None
