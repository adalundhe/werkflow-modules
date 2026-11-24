from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeGuruDisassociateRepositoryRequest(BaseModel):
    AssociationArn: StrictStr
