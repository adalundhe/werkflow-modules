from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_available_upgrade import SageMakerAvailableUpgrade
from .sage_maker_error_info import SageMakerErrorInfo
from .sage_maker_idc_config_output import SageMakerIdcConfigOutput
from .sage_maker_partner_app_config import SageMakerPartnerAppConfig
from .sage_maker_partner_app_maintenance_config import SageMakerPartnerAppMaintenanceConfig


class SageMakerDescribePartnerAppResponse(BaseModel):
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    Status: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    LastModifiedTime: datetime.datetime | StrictStr | None = None
    ExecutionRoleArn: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    BaseUrl: StrictStr | None = None
    MaintenanceConfig: SageMakerPartnerAppMaintenanceConfig | None = None
    Tier: StrictStr | None = None
    Version: StrictStr | None = None
    ApplicationConfig: SageMakerPartnerAppConfig | None = None
    AuthType: StrictStr | None = None
    EnableIamSessionBasedIdentity: StrictBool | None = None
    Error: SageMakerErrorInfo | None = None
    EnableAutoMinorVersionUpgrade: StrictBool | None = None
    CurrentVersionEolDate: datetime.datetime | StrictStr | None = None
    AvailableUpgrade: SageMakerAvailableUpgrade | None = None
    IdcConfig: SageMakerIdcConfigOutput | None = None
    ResponseMetadata: dict[str, Any] | None = None
