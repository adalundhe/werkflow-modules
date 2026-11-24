from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .config_service_conformance_pack_input_parameter import ConfigServiceConformancePackInputParameter
from .config_service_conformance_pack_scope import ConfigServiceConformancePackScope
from .config_service_conformance_pack_source import ConfigServiceConformancePackSource
from .config_service_tag import ConfigServiceTag
from .config_service_template_ssm_document_details import ConfigServiceTemplateSSMDocumentDetails


class ConfigServicePutConformancePackRequest(BaseModel):
    ConformancePackName: StrictStr
    TemplateS3Uri: StrictStr | None = None
    TemplateBody: StrictStr | None = None
    DeliveryS3Bucket: StrictStr | None = None
    DeliveryS3KeyPrefix: StrictStr | None = None
    ConformancePackInputParameters: list[ConfigServiceConformancePackInputParameter] | None = None
    TemplateSSMDocumentDetails: ConfigServiceTemplateSSMDocumentDetails | None = None
    Tags: list[ConfigServiceTag] | None = None
    Source: ConfigServiceConformancePackSource | None = None
    Scope: ConfigServiceConformancePackScope | None = None
