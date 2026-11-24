from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .eks_addon_health import EKSAddonHealth
from .eks_addon_namespace_config_response import EKSAddonNamespaceConfigResponse
from .eks_addon_status import EKSAddonStatus
from .eks_marketplace_information import EKSMarketplaceInformation


class EKSAddon(BaseModel):
    addonName: StrictStr | None = None
    clusterName: StrictStr | None = None
    status: EKSAddonStatus | None = None
    addonVersion: StrictStr | None = None
    health: EKSAddonHealth | None = None
    addonArn: StrictStr | None = None
    createdAt: datetime.datetime | None = None
    modifiedAt: datetime.datetime | None = None
    serviceAccountRoleArn: StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
    publisher: StrictStr | None = None
    owner: StrictStr | None = None
    marketplaceInformation: EKSMarketplaceInformation | None = None
    configurationValues: StrictStr | None = None
    podIdentityAssociations: list[StrictStr] | None = None
    namespaceConfig: EKSAddonNamespaceConfigResponse | None = None
