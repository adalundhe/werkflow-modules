from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeGuruDescribeRepositoryAssociationRequest(BaseModel):
    AssociationArn: StrictStr
