from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .quick_sight_asset_bundle_cloud_formation_override_property_configuration import QuickSightAssetBundleCloudFormationOverridePropertyConfiguration
from .quick_sight_asset_bundle_export_job_validation_strategy import QuickSightAssetBundleExportJobValidationStrategy


class QuickSightStartAssetBundleExportJobRequest(BaseModel):
    AwsAccountId: StrictStr
    AssetBundleExportJobId: StrictStr
    ResourceArns: list[StrictStr]
    ExportFormat: Literal['CLOUDFORMATION_JSON', 'QUICKSIGHT_JSON']
    IncludeAllDependencies: StrictBool | None = None
    CloudFormationOverridePropertyConfiguration: QuickSightAssetBundleCloudFormationOverridePropertyConfiguration | None = None
    IncludePermissions: StrictBool | None = None
    IncludeTags: StrictBool | None = None
    ValidationStrategy: QuickSightAssetBundleExportJobValidationStrategy | None = None
    IncludeFolderMemberships: StrictBool | None = None
    IncludeFolderMembers: Literal['RECURSE', 'ONE_LEVEL', 'NONE'] | None = None
