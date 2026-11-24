from __future__ import annotations
from pydantic import BaseModel
from .connect_agent_quality_metrics import ConnectAgentQualityMetrics
from .connect_customer_quality_metrics import ConnectCustomerQualityMetrics


class ConnectQualityMetrics(BaseModel):
    Agent: ConnectAgentQualityMetrics | None = None
    Customer: ConnectCustomerQualityMetrics | None = None
