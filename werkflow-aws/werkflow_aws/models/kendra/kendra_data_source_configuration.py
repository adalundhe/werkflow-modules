from __future__ import annotations
from pydantic import BaseModel
from .kendra_alfresco_configuration import KendraAlfrescoConfiguration
from .kendra_box_configuration import KendraBoxConfiguration
from .kendra_confluence_configuration import KendraConfluenceConfiguration
from .kendra_database_configuration import KendraDatabaseConfiguration
from .kendra_fsx_configuration import KendraFsxConfiguration
from .kendra_git_hub_configuration import KendraGitHubConfiguration
from .kendra_google_drive_configuration import KendraGoogleDriveConfiguration
from .kendra_jira_configuration import KendraJiraConfiguration
from .kendra_one_drive_configuration import KendraOneDriveConfiguration
from .kendra_quip_configuration import KendraQuipConfiguration
from .kendra_s3_data_source_configuration import KendraS3DataSourceConfiguration
from .kendra_salesforce_configuration import KendraSalesforceConfiguration
from .kendra_service_now_configuration import KendraServiceNowConfiguration
from .kendra_share_point_configuration import KendraSharePointConfiguration
from .kendra_slack_configuration import KendraSlackConfiguration
from .kendra_template_configuration import KendraTemplateConfiguration
from .kendra_web_crawler_configuration import KendraWebCrawlerConfiguration
from .kendra_work_docs_configuration import KendraWorkDocsConfiguration


class KendraDataSourceConfiguration(BaseModel):
    S3Configuration: KendraS3DataSourceConfiguration | None = None
    SharePointConfiguration: KendraSharePointConfiguration | None = None
    DatabaseConfiguration: KendraDatabaseConfiguration | None = None
    SalesforceConfiguration: KendraSalesforceConfiguration | None = None
    OneDriveConfiguration: KendraOneDriveConfiguration | None = None
    ServiceNowConfiguration: KendraServiceNowConfiguration | None = None
    ConfluenceConfiguration: KendraConfluenceConfiguration | None = None
    GoogleDriveConfiguration: KendraGoogleDriveConfiguration | None = None
    WebCrawlerConfiguration: KendraWebCrawlerConfiguration | None = None
    WorkDocsConfiguration: KendraWorkDocsConfiguration | None = None
    FsxConfiguration: KendraFsxConfiguration | None = None
    SlackConfiguration: KendraSlackConfiguration | None = None
    BoxConfiguration: KendraBoxConfiguration | None = None
    QuipConfiguration: KendraQuipConfiguration | None = None
    JiraConfiguration: KendraJiraConfiguration | None = None
    GitHubConfiguration: KendraGitHubConfiguration | None = None
    AlfrescoConfiguration: KendraAlfrescoConfiguration | None = None
    TemplateConfiguration: KendraTemplateConfiguration | None = None
