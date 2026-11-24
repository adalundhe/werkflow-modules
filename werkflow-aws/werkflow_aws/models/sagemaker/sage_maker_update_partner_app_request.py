from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_idc_config_input import SageMakerIdcConfigInput
from .sage_maker_partner_app_config import SageMakerPartnerAppConfig
from .sage_maker_partner_app_maintenance_config import SageMakerPartnerAppMaintenanceConfig
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerUpdatePartnerAppRequest(BaseModel):
    Arn: StrictStr
    MaintenanceConfig: SageMakerPartnerAppMaintenanceConfig | None = None
    Tier: StrictStr | None = None
    ApplicationConfig: SageMakerPartnerAppConfig | None = None
    IdcConfig: SageMakerIdcConfigInput | None = None
    AuthType: Literal['IAM', 'IDC'] | None = None
    EnableIamSessionBasedIdentity: StrictBool | None = None
    EnableAutoMinorVersionUpgrade: StrictBool | None = None
    AppVersion: StrictStr | None = None
    ClientToken: StrictStr | None = None
    Tags: list[SageMakerTagModel] | None = None
