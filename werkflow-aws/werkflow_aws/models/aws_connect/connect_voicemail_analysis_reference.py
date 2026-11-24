from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectVoicemailAnalysisReference(BaseModel):
    Name: StrictStr | None = None
    Value: StrictStr | None = None
    Status: StrictStr | None = None
    Arn: StrictStr | None = None
