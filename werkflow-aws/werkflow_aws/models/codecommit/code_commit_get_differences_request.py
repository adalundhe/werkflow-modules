from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CodeCommitGetDifferencesRequest(BaseModel):
    repositoryName: StrictStr
    afterCommitSpecifier: StrictStr
    beforeCommitSpecifier: StrictStr | None = None
    beforePath: StrictStr | None = None
    afterPath: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
