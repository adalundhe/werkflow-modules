from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeGuruDescribeCodeReviewRequest(BaseModel):
    CodeReviewArn: StrictStr
