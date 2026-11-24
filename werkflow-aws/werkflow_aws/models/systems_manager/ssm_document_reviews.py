from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .ssm_document_review_comment_source import SSMDocumentReviewCommentSource


class SSMDocumentReviews(BaseModel):
    Action: Literal['SendForReview', 'UpdateReview', 'Approve', 'Reject']
    Comment: list[SSMDocumentReviewCommentSource] | None = None
