from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .io_t_audit_check_configuration import IoTAuditCheckConfiguration
from .io_t_audit_notification_target import IoTAuditNotificationTarget


class IoTUpdateAccountAuditConfigurationRequest(BaseModel):
    roleArn: StrictStr | None = None
    auditNotificationTargetConfigurations: dict[Literal['SNS'], IoTAuditNotificationTarget] | None = None
    auditCheckConfigurations: dict[StrictStr, IoTAuditCheckConfiguration] | None = None
