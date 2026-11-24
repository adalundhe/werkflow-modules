from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .dms_data_provider_descriptor import DMSDataProviderDescriptor
from .dmssc_application_attributes import DMSSCApplicationAttributes


class DMSMigrationProject(BaseModel):
    MigrationProjectName: StrictStr | None = None
    MigrationProjectArn: StrictStr | None = None
    MigrationProjectCreationTime: datetime.datetime | StrictStr | None = None
    SourceDataProviderDescriptors: list[DMSDataProviderDescriptor] | None = None
    TargetDataProviderDescriptors: list[DMSDataProviderDescriptor] | None = None
    InstanceProfileArn: StrictStr | None = None
    InstanceProfileName: StrictStr | None = None
    TransformationRules: StrictStr | None = None
    Description: StrictStr | None = None
    SchemaConversionApplicationAttributes: DMSSCApplicationAttributes | None = None
