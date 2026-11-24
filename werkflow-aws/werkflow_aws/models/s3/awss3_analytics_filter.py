from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .awss3_analytics_and_operator import AWSS3AnalyticsAndOperator
from .awss3_tag_model import AWSS3TagModel


class AWSS3AnalyticsFilter(BaseModel):
    Prefix: StrictStr | None = None
    Tag: AWSS3TagModel | None = None
    And: AWSS3AnalyticsAndOperator | None = None
