from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class JExpEvaluateIssuesJqlMetaDataBean(BaseModel):
    isLast: StrictBool | None = None
    nextPageToken: StrictStr | None = None
