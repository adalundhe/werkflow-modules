from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .connect_analytics_configuration import ConnectAnalyticsConfiguration


class ConnectStartContactConversationalAnalyticsJobRequest(BaseModel):
    InstanceId: StrictStr
    ContactId: StrictStr
    AnalyticsModes: list[Literal['PostContact', 'RealTime', 'ContactLens', 'AutomatedInteraction']]
    AnalyticsConfiguration: ConnectAnalyticsConfiguration
    ClientToken: StrictStr | None = None
