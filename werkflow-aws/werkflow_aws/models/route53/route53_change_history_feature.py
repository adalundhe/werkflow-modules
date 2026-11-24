from __future__ import annotations
import datetime
from pydantic import BaseModel
from .route53_feature_enablement import Route53FeatureEnablement


class Route53ChangeHistoryFeature(BaseModel):
    Status: Route53FeatureEnablement | None = None
    RetentionStartsAt: datetime.datetime | None = None
