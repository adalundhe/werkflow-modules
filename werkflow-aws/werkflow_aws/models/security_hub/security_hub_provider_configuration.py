from __future__ import annotations
from pydantic import BaseModel
from .security_hub_azure_provider_configuration import SecurityHubAzureProviderConfiguration
from .security_hub_gcp_provider_configuration import SecurityHubGcpProviderConfiguration
from .security_hub_jira_cloud_provider_configuration import SecurityHubJiraCloudProviderConfiguration
from .security_hub_service_now_provider_configuration import SecurityHubServiceNowProviderConfiguration


class SecurityHubProviderConfiguration(BaseModel):
    JiraCloud: SecurityHubJiraCloudProviderConfiguration | None = None
    ServiceNow: SecurityHubServiceNowProviderConfiguration | None = None
    Azure: SecurityHubAzureProviderConfiguration | None = None
    GCP: SecurityHubGcpProviderConfiguration | None = None
