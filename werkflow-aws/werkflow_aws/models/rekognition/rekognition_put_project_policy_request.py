from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionPutProjectPolicyRequest(BaseModel):
    ProjectArn: StrictStr
    PolicyName: StrictStr
    PolicyDocument: StrictStr
    PolicyRevisionId: StrictStr | None = None
