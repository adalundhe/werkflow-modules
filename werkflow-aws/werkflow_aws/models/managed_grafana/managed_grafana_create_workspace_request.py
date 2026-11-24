from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .managed_grafana_network_access_configuration import ManagedGrafanaNetworkAccessConfiguration
from .managed_grafana_vpc_configuration import ManagedGrafanaVpcConfiguration


class ManagedGrafanaCreateWorkspaceRequest(BaseModel):
    accountAccessType: Literal['CURRENT_ACCOUNT', 'ORGANIZATION']
    permissionType: Literal['CUSTOMER_MANAGED', 'SERVICE_MANAGED']
    authenticationProviders: list[Literal['AWS_SSO', 'SAML']]
    clientToken: StrictStr | None = None
    organizationRoleName: StrictStr | None = None
    stackSetName: StrictStr | None = None
    workspaceDataSources: list[Literal['AMAZON_OPENSEARCH_SERVICE', 'CLOUDWATCH', 'PROMETHEUS', 'XRAY', 'TIMESTREAM', 'SITEWISE', 'ATHENA', 'REDSHIFT', 'TWINMAKER']] | None = None
    workspaceDescription: StrictStr | None = None
    workspaceName: StrictStr | None = None
    workspaceNotificationDestinations: list[Literal['SNS']] | None = None
    workspaceOrganizationalUnits: list[StrictStr] | None = None
    workspaceRoleArn: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    vpcConfiguration: ManagedGrafanaVpcConfiguration | None = None
    configuration: StrictStr | None = None
    networkAccessControl: ManagedGrafanaNetworkAccessConfiguration | None = None
    grafanaVersion: StrictStr | None = None
    ipAddressType: Literal['IPv4', 'DualStack'] | None = None
    kmsKeyId: StrictStr | None = None
