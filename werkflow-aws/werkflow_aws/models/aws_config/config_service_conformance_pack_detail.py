from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .config_service_conformance_pack_input_parameter import ConfigServiceConformancePackInputParameter
from .config_service_conformance_pack_scope import ConfigServiceConformancePackScope
from .config_service_conformance_pack_source import ConfigServiceConformancePackSource
from .config_service_template_ssm_document_details import ConfigServiceTemplateSSMDocumentDetails


class ConfigServiceConformancePackDetail(BaseModel):
    ConformancePackName: StrictStr | None = None
    ConformancePackArn: StrictStr | None = None
    ConformancePackId: StrictStr | None = None
    DeliveryS3Bucket: StrictStr | None = None
    DeliveryS3KeyPrefix: StrictStr | None = None
    ConformancePackInputParameters: list[ConfigServiceConformancePackInputParameter] | None = None
    LastUpdateRequestedTime: datetime.datetime | StrictStr | None = None
    CreatedBy: StrictStr | None = None
    TemplateSSMDocumentDetails: ConfigServiceTemplateSSMDocumentDetails | None = None
    Type: StrictStr | None = None
    Source: ConfigServiceConformancePackSource | None = None
    Scope: ConfigServiceConformancePackScope | None = None
