from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_data_source_to_index_field_mapping import KendraDataSourceToIndexFieldMapping


class KendraGoogleDriveConfiguration(BaseModel):
    SecretArn: StrictStr | None = None
    InclusionPatterns: list[StrictStr] | None = None
    ExclusionPatterns: list[StrictStr] | None = None
    FieldMappings: list[KendraDataSourceToIndexFieldMapping] | None = None
    ExcludeMimeTypes: list[StrictStr] | None = None
    ExcludeUserAccounts: list[StrictStr] | None = None
    ExcludeSharedDrives: list[StrictStr] | None = None
