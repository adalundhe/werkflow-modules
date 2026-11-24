from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .kendra_data_source_to_index_field_mapping import KendraDataSourceToIndexFieldMapping
from .kendra_data_source_vpc_configuration import KendraDataSourceVpcConfiguration


class KendraQuipConfiguration(BaseModel):
    Domain: StrictStr | None = None
    SecretArn: StrictStr | None = None
    CrawlFileComments: StrictBool | None = None
    CrawlChatRooms: StrictBool | None = None
    CrawlAttachments: StrictBool | None = None
    FolderIds: list[StrictStr] | None = None
    ThreadFieldMappings: list[KendraDataSourceToIndexFieldMapping] | None = None
    MessageFieldMappings: list[KendraDataSourceToIndexFieldMapping] | None = None
    AttachmentFieldMappings: list[KendraDataSourceToIndexFieldMapping] | None = None
    InclusionPatterns: list[StrictStr] | None = None
    ExclusionPatterns: list[StrictStr] | None = None
    VpcConfiguration: KendraDataSourceVpcConfiguration | None = None
