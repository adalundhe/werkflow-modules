from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .kendra_data_source_to_index_field_mapping import KendraDataSourceToIndexFieldMapping
from .kendra_one_drive_users import KendraOneDriveUsers


class KendraOneDriveConfiguration(BaseModel):
    TenantDomain: StrictStr | None = None
    SecretArn: StrictStr | None = None
    OneDriveUsers: KendraOneDriveUsers | None = None
    InclusionPatterns: list[StrictStr] | None = None
    ExclusionPatterns: list[StrictStr] | None = None
    FieldMappings: list[KendraDataSourceToIndexFieldMapping] | None = None
    DisableLocalGroups: StrictBool | None = None
