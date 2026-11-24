from __future__ import annotations
from pydantic import BaseModel
from .msk_authorizer_logs import MSKAuthorizerLogs
from .msk_broker_logs_model import MSKBrokerLogsModel


class MSKLoggingInfoModel(BaseModel):
    AuthorizerLogs: MSKAuthorizerLogs | None = None
    BrokerLogs: MSKBrokerLogsModel | None = None
