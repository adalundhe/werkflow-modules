from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_data_source_to_index_field_mapping import KendraDataSourceToIndexFieldMapping
from .kendra_data_source_vpc_configuration import KendraDataSourceVpcConfiguration


class KendraFsxConfiguration(BaseModel):
    FileSystemId: StrictStr | None = None
    FileSystemType: StrictStr | None = None
    VpcConfiguration: KendraDataSourceVpcConfiguration | None = None
    SecretArn: StrictStr | None = None
    InclusionPatterns: list[StrictStr] | None = None
    ExclusionPatterns: list[StrictStr] | None = None
    FieldMappings: list[KendraDataSourceToIndexFieldMapping] | None = None
