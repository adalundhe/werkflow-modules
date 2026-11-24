from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMDocumentReviewCommentSource(BaseModel):
    Type: StrictStr | None = None
    Content: StrictStr | None = None
