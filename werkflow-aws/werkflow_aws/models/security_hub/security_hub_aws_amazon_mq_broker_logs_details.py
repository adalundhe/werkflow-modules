from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .security_hub_aws_amazon_mq_broker_logs_pending_details import SecurityHubAwsAmazonMqBrokerLogsPendingDetails


class SecurityHubAwsAmazonMqBrokerLogsDetails(BaseModel):
    Audit: StrictBool | None = None
    General: StrictBool | None = None
    AuditLogGroup: StrictStr | None = None
    GeneralLogGroup: StrictStr | None = None
    Pending: SecurityHubAwsAmazonMqBrokerLogsPendingDetails | None = None
