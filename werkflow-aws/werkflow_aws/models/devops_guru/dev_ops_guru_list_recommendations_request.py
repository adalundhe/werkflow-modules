from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DevOpsGuruListRecommendationsRequest(BaseModel):
    InsightId: StrictStr
    NextToken: StrictStr | None = None
    Locale: Literal['DE_DE', 'EN_US', 'EN_GB', 'ES_ES', 'FR_FR', 'IT_IT', 'JA_JP', 'KO_KR', 'PT_BR', 'ZH_CN', 'ZH_TW'] | None = None
    AccountId: StrictStr | None = None
