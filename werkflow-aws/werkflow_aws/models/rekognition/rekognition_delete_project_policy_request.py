from __future__ import annotations
from pydantic import BaseModel, StrictStr


class RekognitionDeleteProjectPolicyRequest(BaseModel):
    ProjectArn: StrictStr
    PolicyName: StrictStr
    PolicyRevisionId: StrictStr | None = None
