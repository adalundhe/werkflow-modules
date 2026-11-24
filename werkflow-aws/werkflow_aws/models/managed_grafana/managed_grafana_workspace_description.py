from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .managed_grafana_authentication_summary import ManagedGrafanaAuthenticationSummary
from .managed_grafana_network_access_configuration import ManagedGrafanaNetworkAccessConfiguration
from .managed_grafana_vpc_configuration import ManagedGrafanaVpcConfiguration


class ManagedGrafanaWorkspaceDescription(BaseModel):
    accountAccessType: StrictStr | None = None
    created: datetime.datetime | StrictStr | None = None
    dataSources: list[StrictStr] | None = None
    description: StrictStr | None = None
    endpoint: StrictStr | None = None
    grafanaVersion: StrictStr | None = None
    id: StrictStr | None = None
    modified: datetime.datetime | StrictStr | None = None
    name: StrictStr | None = None
    organizationRoleName: StrictStr | None = None
    notificationDestinations: list[StrictStr] | None = None
    organizationalUnits: list[StrictStr] | None = None
    permissionType: StrictStr | None = None
    stackSetName: StrictStr | None = None
    status: StrictStr | None = None
    workspaceRoleArn: StrictStr | None = None
    licenseType: StrictStr | None = None
    freeTrialConsumed: StrictBool | None = None
    licenseExpiration: datetime.datetime | StrictStr | None = None
    freeTrialExpiration: datetime.datetime | StrictStr | None = None
    authentication: ManagedGrafanaAuthenticationSummary | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    vpcConfiguration: ManagedGrafanaVpcConfiguration | None = None
    networkAccessControl: ManagedGrafanaNetworkAccessConfiguration | None = None
    grafanaToken: StrictStr | None = None
    ipAddressType: StrictStr | None = None
    kmsKeyId: StrictStr | None = None
    degradedWorkspaceReason: StrictStr | None = None
