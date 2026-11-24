from __future__ import annotations
from pydantic import BaseModel
from .macie_sensitivity_aggregations import MacieSensitivityAggregations


class MacieBucketStatisticsBySensitivity(BaseModel):
    classificationError: MacieSensitivityAggregations | None = None
    notClassified: MacieSensitivityAggregations | None = None
    notSensitive: MacieSensitivityAggregations | None = None
    sensitive: MacieSensitivityAggregations | None = None
