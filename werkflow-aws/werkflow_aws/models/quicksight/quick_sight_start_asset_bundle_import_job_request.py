from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .quick_sight_asset_bundle_import_job_override_parameters import QuickSightAssetBundleImportJobOverrideParameters
from .quick_sight_asset_bundle_import_job_override_permissions import QuickSightAssetBundleImportJobOverridePermissions
from .quick_sight_asset_bundle_import_job_override_tags import QuickSightAssetBundleImportJobOverrideTags
from .quick_sight_asset_bundle_import_job_override_validation_strategy import QuickSightAssetBundleImportJobOverrideValidationStrategy
from .quick_sight_asset_bundle_import_source import QuickSightAssetBundleImportSource


class QuickSightStartAssetBundleImportJobRequest(BaseModel):
    AwsAccountId: StrictStr
    AssetBundleImportJobId: StrictStr
    AssetBundleImportSource: QuickSightAssetBundleImportSource
    OverrideParameters: QuickSightAssetBundleImportJobOverrideParameters | None = None
    FailureAction: Literal['DO_NOTHING', 'ROLLBACK'] | None = None
    OverridePermissions: QuickSightAssetBundleImportJobOverridePermissions | None = None
    OverrideTags: QuickSightAssetBundleImportJobOverrideTags | None = None
    OverrideValidationStrategy: QuickSightAssetBundleImportJobOverrideValidationStrategy | None = None
