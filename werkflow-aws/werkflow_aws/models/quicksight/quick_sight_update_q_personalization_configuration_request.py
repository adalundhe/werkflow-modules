from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QuickSightUpdateQPersonalizationConfigurationRequest(BaseModel):
    AwsAccountId: StrictStr
    PersonalizationMode: Literal['ENABLED', 'DISABLED']
