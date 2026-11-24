from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .managed_grafana_network_access_configuration import ManagedGrafanaNetworkAccessConfiguration
from .managed_grafana_vpc_configuration import ManagedGrafanaVpcConfiguration


class ManagedGrafanaUpdateWorkspaceRequest(BaseModel):
    workspaceId: StrictStr
    accountAccessType: Literal['CURRENT_ACCOUNT', 'ORGANIZATION'] | None = None
    organizationRoleName: StrictStr | None = None
    permissionType: Literal['CUSTOMER_MANAGED', 'SERVICE_MANAGED'] | None = None
    stackSetName: StrictStr | None = None
    workspaceDataSources: list[Literal['AMAZON_OPENSEARCH_SERVICE', 'CLOUDWATCH', 'PROMETHEUS', 'XRAY', 'TIMESTREAM', 'SITEWISE', 'ATHENA', 'REDSHIFT', 'TWINMAKER']] | None = None
    workspaceDescription: StrictStr | None = None
    workspaceName: StrictStr | None = None
    workspaceNotificationDestinations: list[Literal['SNS']] | None = None
    workspaceOrganizationalUnits: list[StrictStr] | None = None
    workspaceRoleArn: StrictStr | None = None
    vpcConfiguration: ManagedGrafanaVpcConfiguration | None = None
    removeVpcConfiguration: StrictBool | None = None
    networkAccessControl: ManagedGrafanaNetworkAccessConfiguration | None = None
    removeNetworkAccessConfiguration: StrictBool | None = None
    ipAddressType: Literal['IPv4', 'DualStack'] | None = None
