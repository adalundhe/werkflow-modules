from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ssm_document_review_comment_source import SSMDocumentReviewCommentSource


class SSMDocumentReviewerResponseSource(BaseModel):
    CreateTime: datetime.datetime | StrictStr | None = None
    UpdatedTime: datetime.datetime | StrictStr | None = None
    ReviewStatus: StrictStr | None = None
    Comment: list[SSMDocumentReviewCommentSource] | None = None
    Reviewer: StrictStr | None = None
