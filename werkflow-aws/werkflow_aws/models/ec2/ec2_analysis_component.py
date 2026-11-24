from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2AnalysisComponent(BaseModel):
    Id: StrictStr | None = None
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
