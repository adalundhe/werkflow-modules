from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class WAFv2AWSManagedRulesBotControlRuleSet(BaseModel):
    InspectionLevel: StrictStr | None = None
    EnableMachineLearning: StrictBool | None = None
