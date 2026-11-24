from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .connect_evaluation_review_request_comment import ConnectEvaluationReviewRequestComment


class ConnectEvaluationReviewMetadata(BaseModel):
    ReviewId: StrictStr | None = None
    RequestedTime: datetime.datetime | StrictStr | None = None
    RequestedBy: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    CreatedBy: StrictStr | None = None
    ReviewRequestComments: list[ConnectEvaluationReviewRequestComment] | None = None
