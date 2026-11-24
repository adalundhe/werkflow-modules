from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .security_hub_aws_open_search_service_domain_master_user_options_details import SecurityHubAwsOpenSearchServiceDomainMasterUserOptionsDetails


class SecurityHubAwsOpenSearchServiceDomainAdvancedSecurityOptionsDetails(BaseModel):
    Enabled: StrictBool | None = None
    InternalUserDatabaseEnabled: StrictBool | None = None
    MasterUserOptions: SecurityHubAwsOpenSearchServiceDomainMasterUserOptionsDetails | None = None
