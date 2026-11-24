from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .code_guru_code_review_type import CodeGuruCodeReviewType


class CodeGuruCreateCodeReviewRequest(BaseModel):
    Name: StrictStr
    RepositoryAssociationArn: StrictStr
    Type: CodeGuruCodeReviewType
    ClientRequestToken: StrictStr | None = None
