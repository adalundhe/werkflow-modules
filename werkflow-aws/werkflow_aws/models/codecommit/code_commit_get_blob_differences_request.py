from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class CodeCommitGetBlobDifferencesRequest(BaseModel):
    repositoryName: StrictStr
    afterBlobId: StrictStr
    beforeBlobId: StrictStr | None = None
    contextLines: StrictInt | None = None
    ignoreWhitespace: StrictBool | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
