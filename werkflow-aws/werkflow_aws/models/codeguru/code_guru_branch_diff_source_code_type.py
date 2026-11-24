from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeGuruBranchDiffSourceCodeType(BaseModel):
    SourceBranchName: StrictStr | None = None
    DestinationBranchName: StrictStr | None = None
