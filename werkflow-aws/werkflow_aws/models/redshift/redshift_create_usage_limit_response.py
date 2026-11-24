from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .redshift_tag import RedshiftTag


class RedshiftCreateUsageLimitResponse(BaseModel):
    UsageLimitId: StrictStr | None = None
    ClusterIdentifier: StrictStr | None = None
    FeatureType: StrictStr | None = None
    LimitType: StrictStr | None = None
    Amount: StrictInt | None = None
    Period: StrictStr | None = None
    BreachAction: StrictStr | None = None
    Tags: list[RedshiftTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
