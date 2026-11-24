from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .dms_data_provider_descriptor_definition import DMSDataProviderDescriptorDefinition
from .dmssc_application_attributes import DMSSCApplicationAttributes


class DMSModifyMigrationProjectRequest(BaseModel):
    MigrationProjectIdentifier: StrictStr
    MigrationProjectName: StrictStr | None = None
    SourceDataProviderDescriptors: list[DMSDataProviderDescriptorDefinition] | None = None
    TargetDataProviderDescriptors: list[DMSDataProviderDescriptorDefinition] | None = None
    InstanceProfileIdentifier: StrictStr | None = None
    TransformationRules: StrictStr | None = None
    Description: StrictStr | None = None
    SchemaConversionApplicationAttributes: DMSSCApplicationAttributes | None = None
