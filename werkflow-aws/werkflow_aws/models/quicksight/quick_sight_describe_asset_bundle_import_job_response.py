from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_asset_bundle_import_job_error import QuickSightAssetBundleImportJobError
from .quick_sight_asset_bundle_import_job_override_parameters import QuickSightAssetBundleImportJobOverrideParameters
from .quick_sight_asset_bundle_import_job_override_permissions import QuickSightAssetBundleImportJobOverridePermissions
from .quick_sight_asset_bundle_import_job_override_tags import QuickSightAssetBundleImportJobOverrideTags
from .quick_sight_asset_bundle_import_job_override_validation_strategy import QuickSightAssetBundleImportJobOverrideValidationStrategy
from .quick_sight_asset_bundle_import_job_warning import QuickSightAssetBundleImportJobWarning
from .quick_sight_asset_bundle_import_source_description import QuickSightAssetBundleImportSourceDescription


class QuickSightDescribeAssetBundleImportJobResponse(BaseModel):
    JobStatus: StrictStr | None = None
    Errors: list[QuickSightAssetBundleImportJobError] | None = None
    RollbackErrors: list[QuickSightAssetBundleImportJobError] | None = None
    Arn: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    AssetBundleImportJobId: StrictStr | None = None
    AwsAccountId: StrictStr | None = None
    AssetBundleImportSource: QuickSightAssetBundleImportSourceDescription | None = None
    OverrideParameters: QuickSightAssetBundleImportJobOverrideParameters | None = None
    FailureAction: StrictStr | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    OverridePermissions: QuickSightAssetBundleImportJobOverridePermissions | None = None
    OverrideTags: QuickSightAssetBundleImportJobOverrideTags | None = None
    OverrideValidationStrategy: QuickSightAssetBundleImportJobOverrideValidationStrategy | None = None
    Warnings: list[QuickSightAssetBundleImportJobWarning] | None = None
    ResponseMetadata: dict[str, Any] | None = None
