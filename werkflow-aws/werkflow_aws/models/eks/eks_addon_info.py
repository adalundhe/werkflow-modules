from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .eks_addon_version_info import EKSAddonVersionInfo
from .eks_marketplace_information_model import EKSMarketplaceInformationModel


class EKSAddonInfo(BaseModel):
    addonName: StrictStr | None = None
    type: StrictStr | None = None
    addonVersions: list[EKSAddonVersionInfo] | None = None
    publisher: StrictStr | None = None
    owner: StrictStr | None = None
    marketplaceInformation: EKSMarketplaceInformationModel | None = None
    defaultNamespace: StrictStr | None = None
