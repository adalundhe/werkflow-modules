from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_audit_check_configuration import IoTAuditCheckConfiguration
from .io_t_audit_notification_target import IoTAuditNotificationTarget


class IoTDescribeAccountAuditConfigurationResponse(BaseModel):
    roleArn: StrictStr | None = None
    auditNotificationTargetConfigurations: dict[StrictStr, IoTAuditNotificationTarget] | None = None
    auditCheckConfigurations: dict[StrictStr, IoTAuditCheckConfiguration] | None = None
    ResponseMetadata: dict[str, Any] | None = None
