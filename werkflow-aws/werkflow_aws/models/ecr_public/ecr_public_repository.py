from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ECRPublicRepository(BaseModel):
    repositoryArn: StrictStr | None = None
    registryId: StrictStr | None = None
    repositoryName: StrictStr | None = None
    repositoryUri: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
