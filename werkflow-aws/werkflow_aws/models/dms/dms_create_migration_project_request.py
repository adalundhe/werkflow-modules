from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dms_data_provider_descriptor_definition import DMSDataProviderDescriptorDefinition
from .dmssc_application_attributes import DMSSCApplicationAttributes
from .dms_tag import DMSTag


class DMSCreateMigrationProjectRequest(BaseModel):
    SourceDataProviderDescriptors: list[DMSDataProviderDescriptorDefinition]
    TargetDataProviderDescriptors: list[DMSDataProviderDescriptorDefinition]
    InstanceProfileIdentifier: StrictStr
    MigrationProjectName: StrictStr | None = None
    TransformationRules: StrictStr | None = None
    Description: StrictStr | None = None
    Tags: list[DMSTag] | None = None
    SchemaConversionApplicationAttributes: DMSSCApplicationAttributes | None = None
