from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_asset_bundle_resource_permissions import QuickSightAssetBundleResourcePermissions


class QuickSightAssetBundleImportJobThemeOverridePermissions(BaseModel):
    ThemeIds: list[StrictStr] | None = None
    Permissions: QuickSightAssetBundleResourcePermissions | None = None
