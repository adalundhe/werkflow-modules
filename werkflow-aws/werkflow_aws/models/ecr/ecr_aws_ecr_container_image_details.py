from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class ECRAwsEcrContainerImageDetails(BaseModel):
    architecture: StrictStr | None = None
    author: StrictStr | None = None
    imageHash: StrictStr | None = None
    imageTags: list[StrictStr] | None = None
    platform: StrictStr | None = None
    pushedAt: datetime.datetime | StrictStr | None = None
    lastInUseAt: datetime.datetime | StrictStr | None = None
    inUseCount: StrictInt | None = None
    registry: StrictStr | None = None
    repositoryName: StrictStr | None = None
