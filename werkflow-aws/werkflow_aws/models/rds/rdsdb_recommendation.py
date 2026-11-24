from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .rds_doc_link import RDSDocLink
from .rds_issue_details import RDSIssueDetails
from .rds_recommended_action import RDSRecommendedAction


class RDSDBRecommendation(BaseModel):
    RecommendationId: StrictStr | None = None
    TypeId: StrictStr | None = None
    Severity: StrictStr | None = None
    ResourceArn: StrictStr | None = None
    Status: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    UpdatedTime: datetime.datetime | StrictStr | None = None
    Detection: StrictStr | None = None
    Recommendation: StrictStr | None = None
    Description: StrictStr | None = None
    Reason: StrictStr | None = None
    RecommendedActions: list[RDSRecommendedAction] | None = None
    Category: StrictStr | None = None
    Source: StrictStr | None = None
    TypeDetection: StrictStr | None = None
    TypeRecommendation: StrictStr | None = None
    Impact: StrictStr | None = None
    AdditionalInfo: StrictStr | None = None
    Links: list[RDSDocLink] | None = None
    IssueDetails: RDSIssueDetails | None = None
