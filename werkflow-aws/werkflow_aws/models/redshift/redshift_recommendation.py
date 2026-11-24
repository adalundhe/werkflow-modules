from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .redshift_recommended_action import RedshiftRecommendedAction
from .redshift_reference_link import RedshiftReferenceLink


class RedshiftRecommendation(BaseModel):
    Id: StrictStr | None = None
    ClusterIdentifier: StrictStr | None = None
    NamespaceArn: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    RecommendationType: StrictStr | None = None
    Title: StrictStr | None = None
    Description: StrictStr | None = None
    Observation: StrictStr | None = None
    ImpactRanking: StrictStr | None = None
    RecommendationText: StrictStr | None = None
    RecommendedActions: list[RedshiftRecommendedAction] | None = None
    ReferenceLinks: list[RedshiftReferenceLink] | None = None
