from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AccessAnalyzerPolicyGenerationDetails(BaseModel):
    principalArn: StrictStr
