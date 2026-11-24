from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .kendra_data_source_to_index_field_mapping import KendraDataSourceToIndexFieldMapping
from .kendra_data_source_vpc_configuration import KendraDataSourceVpcConfiguration


class KendraJiraConfiguration(BaseModel):
    JiraAccountUrl: StrictStr | None = None
    SecretArn: StrictStr | None = None
    UseChangeLog: StrictBool | None = None
    Project: list[StrictStr] | None = None
    IssueType: list[StrictStr] | None = None
    Status: list[StrictStr] | None = None
    IssueSubEntityFilter: list[StrictStr] | None = None
    AttachmentFieldMappings: list[KendraDataSourceToIndexFieldMapping] | None = None
    CommentFieldMappings: list[KendraDataSourceToIndexFieldMapping] | None = None
    IssueFieldMappings: list[KendraDataSourceToIndexFieldMapping] | None = None
    ProjectFieldMappings: list[KendraDataSourceToIndexFieldMapping] | None = None
    WorkLogFieldMappings: list[KendraDataSourceToIndexFieldMapping] | None = None
    InclusionPatterns: list[StrictStr] | None = None
    ExclusionPatterns: list[StrictStr] | None = None
    VpcConfiguration: KendraDataSourceVpcConfiguration | None = None
