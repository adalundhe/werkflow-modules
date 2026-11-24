from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .config_service_conformance_pack_input_parameter import ConfigServiceConformancePackInputParameter


class ConfigServiceOrganizationConformancePack(BaseModel):
    OrganizationConformancePackName: StrictStr | None = None
    OrganizationConformancePackArn: StrictStr | None = None
    DeliveryS3Bucket: StrictStr | None = None
    DeliveryS3KeyPrefix: StrictStr | None = None
    ConformancePackInputParameters: list[ConfigServiceConformancePackInputParameter] | None = None
    ExcludedAccounts: list[StrictStr] | None = None
    LastUpdateTime: datetime.datetime | StrictStr | None = None
