from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueSourceControlDetails(BaseModel):
    Provider: StrictStr | None = None
    Repository: StrictStr | None = None
    Owner: StrictStr | None = None
    Branch: StrictStr | None = None
    Folder: StrictStr | None = None
    LastCommitId: StrictStr | None = None
    AuthStrategy: StrictStr | None = None
    AuthToken: StrictStr | None = None
