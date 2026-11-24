from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .kendra_data_source_to_index_field_mapping import KendraDataSourceToIndexFieldMapping
from .kendra_data_source_vpc_configuration import KendraDataSourceVpcConfiguration
from .kendra_git_hub_document_crawl_properties import KendraGitHubDocumentCrawlProperties
from .kendra_on_premise_configuration import KendraOnPremiseConfiguration
from .kendra_saa_s_configuration import KendraSaaSConfiguration


class KendraGitHubConfiguration(BaseModel):
    SaaSConfiguration: KendraSaaSConfiguration | None = None
    OnPremiseConfiguration: KendraOnPremiseConfiguration | None = None
    Type: StrictStr | None = None
    SecretArn: StrictStr | None = None
    UseChangeLog: StrictBool | None = None
    GitHubDocumentCrawlProperties: KendraGitHubDocumentCrawlProperties | None = None
    RepositoryFilter: list[StrictStr] | None = None
    InclusionFolderNamePatterns: list[StrictStr] | None = None
    InclusionFileTypePatterns: list[StrictStr] | None = None
    InclusionFileNamePatterns: list[StrictStr] | None = None
    ExclusionFolderNamePatterns: list[StrictStr] | None = None
    ExclusionFileTypePatterns: list[StrictStr] | None = None
    ExclusionFileNamePatterns: list[StrictStr] | None = None
    VpcConfiguration: KendraDataSourceVpcConfiguration | None = None
    GitHubRepositoryConfigurationFieldMappings: list[KendraDataSourceToIndexFieldMapping] | None = None
    GitHubCommitConfigurationFieldMappings: list[KendraDataSourceToIndexFieldMapping] | None = None
    GitHubIssueDocumentConfigurationFieldMappings: list[KendraDataSourceToIndexFieldMapping] | None = None
    GitHubIssueCommentConfigurationFieldMappings: list[KendraDataSourceToIndexFieldMapping] | None = None
    GitHubIssueAttachmentConfigurationFieldMappings: list[KendraDataSourceToIndexFieldMapping] | None = None
    GitHubPullRequestCommentConfigurationFieldMappings: list[KendraDataSourceToIndexFieldMapping] | None = None
    GitHubPullRequestDocumentConfigurationFieldMappings: list[KendraDataSourceToIndexFieldMapping] | None = None
    GitHubPullRequestDocumentAttachmentConfigurationFieldMappings: list[KendraDataSourceToIndexFieldMapping] | None = None
