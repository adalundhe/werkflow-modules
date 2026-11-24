from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .quick_sight_asset_bundle_cloud_formation_override_property_configuration import QuickSightAssetBundleCloudFormationOverridePropertyConfiguration
from .quick_sight_asset_bundle_export_job_error import QuickSightAssetBundleExportJobError
from .quick_sight_asset_bundle_export_job_validation_strategy import QuickSightAssetBundleExportJobValidationStrategy
from .quick_sight_asset_bundle_export_job_warning import QuickSightAssetBundleExportJobWarning


class QuickSightDescribeAssetBundleExportJobResponse(BaseModel):
    JobStatus: StrictStr | None = None
    DownloadUrl: StrictStr | None = None
    Errors: list[QuickSightAssetBundleExportJobError] | None = None
    Arn: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    AssetBundleExportJobId: StrictStr | None = None
    AwsAccountId: StrictStr | None = None
    ResourceArns: list[StrictStr] | None = None
    IncludeAllDependencies: StrictBool | None = None
    ExportFormat: StrictStr | None = None
    CloudFormationOverridePropertyConfiguration: QuickSightAssetBundleCloudFormationOverridePropertyConfiguration | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    IncludePermissions: StrictBool | None = None
    IncludeTags: StrictBool | None = None
    ValidationStrategy: QuickSightAssetBundleExportJobValidationStrategy | None = None
    Warnings: list[QuickSightAssetBundleExportJobWarning] | None = None
    IncludeFolderMemberships: StrictBool | None = None
    IncludeFolderMembers: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
