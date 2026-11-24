from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .awss3_metrics_and_operator import AWSS3MetricsAndOperator
from .awss3_tag_model import AWSS3TagModel


class AWSS3MetricsFilter(BaseModel):
    Prefix: StrictStr | None = None
    Tag: AWSS3TagModel | None = None
    AccessPointArn: StrictStr | None = None
    And: AWSS3MetricsAndOperator | None = None
