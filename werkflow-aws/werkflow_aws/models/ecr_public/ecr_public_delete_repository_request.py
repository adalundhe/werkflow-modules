from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ECRPublicDeleteRepositoryRequest(BaseModel):
    repositoryName: StrictStr
    registryId: StrictStr | None = None
    force: StrictBool | None = None
