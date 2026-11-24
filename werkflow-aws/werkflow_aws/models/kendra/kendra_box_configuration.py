from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .kendra_data_source_to_index_field_mapping import KendraDataSourceToIndexFieldMapping
from .kendra_data_source_vpc_configuration import KendraDataSourceVpcConfiguration


class KendraBoxConfiguration(BaseModel):
    EnterpriseId: StrictStr | None = None
    SecretArn: StrictStr | None = None
    UseChangeLog: StrictBool | None = None
    CrawlComments: StrictBool | None = None
    CrawlTasks: StrictBool | None = None
    CrawlWebLinks: StrictBool | None = None
    FileFieldMappings: list[KendraDataSourceToIndexFieldMapping] | None = None
    TaskFieldMappings: list[KendraDataSourceToIndexFieldMapping] | None = None
    CommentFieldMappings: list[KendraDataSourceToIndexFieldMapping] | None = None
    WebLinkFieldMappings: list[KendraDataSourceToIndexFieldMapping] | None = None
    InclusionPatterns: list[StrictStr] | None = None
    ExclusionPatterns: list[StrictStr] | None = None
    VpcConfiguration: KendraDataSourceVpcConfiguration | None = None
