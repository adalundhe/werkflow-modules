from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .kendra_data_source_to_index_field_mapping import KendraDataSourceToIndexFieldMapping
from .kendra_data_source_vpc_configuration import KendraDataSourceVpcConfiguration


class KendraSlackConfiguration(BaseModel):
    TeamId: StrictStr | None = None
    SecretArn: StrictStr | None = None
    VpcConfiguration: KendraDataSourceVpcConfiguration | None = None
    SlackEntityList: list[StrictStr] | None = None
    UseChangeLog: StrictBool | None = None
    CrawlBotMessage: StrictBool | None = None
    ExcludeArchived: StrictBool | None = None
    SinceCrawlDate: StrictStr | None = None
    LookBackPeriod: StrictInt | None = None
    PrivateChannelFilter: list[StrictStr] | None = None
    PublicChannelFilter: list[StrictStr] | None = None
    InclusionPatterns: list[StrictStr] | None = None
    ExclusionPatterns: list[StrictStr] | None = None
    FieldMappings: list[KendraDataSourceToIndexFieldMapping] | None = None
