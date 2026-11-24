from __future__ import annotations
from pydantic import BaseModel
from .security_hub_azure_update_configuration import SecurityHubAzureUpdateConfiguration
from .security_hub_gcp_update_configuration import SecurityHubGcpUpdateConfiguration
from .security_hub_jira_cloud_update_configuration import SecurityHubJiraCloudUpdateConfiguration
from .security_hub_service_now_update_configuration import SecurityHubServiceNowUpdateConfiguration


class SecurityHubProviderUpdateConfiguration(BaseModel):
    JiraCloud: SecurityHubJiraCloudUpdateConfiguration | None = None
    ServiceNow: SecurityHubServiceNowUpdateConfiguration | None = None
    Azure: SecurityHubAzureUpdateConfiguration | None = None
    GCP: SecurityHubGcpUpdateConfiguration | None = None
