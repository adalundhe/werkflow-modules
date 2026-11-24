from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ECRPublicDescribeImageTagsRequest(BaseModel):
    repositoryName: StrictStr
    registryId: StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
