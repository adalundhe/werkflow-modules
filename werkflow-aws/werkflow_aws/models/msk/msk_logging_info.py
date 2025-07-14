from pydantic import BaseModel
from .msk_broker_logs import MSKBrokerLogs


class MSKLoggingInfo(BaseModel):
    BrokerLogs: MSKBrokerLogs