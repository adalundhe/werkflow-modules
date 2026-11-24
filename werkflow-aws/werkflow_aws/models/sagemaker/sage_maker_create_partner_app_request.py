from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .sage_maker_idc_config_input import SageMakerIdcConfigInput
from .sage_maker_partner_app_config import SageMakerPartnerAppConfig
from .sage_maker_partner_app_maintenance_config import SageMakerPartnerAppMaintenanceConfig
from .sage_maker_tag_model import SageMakerTagModel


class SageMakerCreatePartnerAppRequest(BaseModel):
    Name: StrictStr
    Type: Literal['lakera-guard', 'comet', 'deepchecks-llm-evaluation', 'fiddler']
    ExecutionRoleArn: StrictStr
    Tier: StrictStr
    AuthType: Literal['IAM', 'IDC']
    KmsKeyId: StrictStr | None = None
    MaintenanceConfig: SageMakerPartnerAppMaintenanceConfig | None = None
    ApplicationConfig: SageMakerPartnerAppConfig | None = None
    IdcConfig: SageMakerIdcConfigInput | None = None
    EnableIamSessionBasedIdentity: StrictBool | None = None
    EnableAutoMinorVersionUpgrade: StrictBool | None = None
    ClientToken: StrictStr | None = None
    Tags: list[SageMakerTagModel] | None = None
