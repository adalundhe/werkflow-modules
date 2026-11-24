from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class DetectiveListIndicatorsRequest(BaseModel):
    GraphArn: StrictStr
    InvestigationId: StrictStr
    IndicatorType: Literal['TTP_OBSERVED', 'IMPOSSIBLE_TRAVEL', 'FLAGGED_IP_ADDRESS', 'NEW_GEOLOCATION', 'NEW_ASO', 'NEW_USER_AGENT', 'RELATED_FINDING', 'RELATED_FINDING_GROUP'] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
