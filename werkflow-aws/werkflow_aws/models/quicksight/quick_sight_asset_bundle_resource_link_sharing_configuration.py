from __future__ import annotations
from pydantic import BaseModel
from .quick_sight_asset_bundle_resource_permissions import QuickSightAssetBundleResourcePermissions


class QuickSightAssetBundleResourceLinkSharingConfiguration(BaseModel):
    Permissions: QuickSightAssetBundleResourcePermissions | None = None
