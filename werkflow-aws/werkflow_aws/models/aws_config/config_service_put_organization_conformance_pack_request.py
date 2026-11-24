from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .config_service_conformance_pack_input_parameter import ConfigServiceConformancePackInputParameter
from .config_service_tag import ConfigServiceTag


class ConfigServicePutOrganizationConformancePackRequest(BaseModel):
    OrganizationConformancePackName: StrictStr
    TemplateS3Uri: StrictStr | None = None
    TemplateBody: StrictStr | None = None
    DeliveryS3Bucket: StrictStr | None = None
    DeliveryS3KeyPrefix: StrictStr | None = None
    ConformancePackInputParameters: list[ConfigServiceConformancePackInputParameter] | None = None
    ExcludedAccounts: list[StrictStr] | None = None
    Tags: list[ConfigServiceTag] | None = None
