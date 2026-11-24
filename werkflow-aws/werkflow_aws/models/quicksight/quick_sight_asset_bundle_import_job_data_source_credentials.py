from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_asset_bundle_import_job_data_source_credential_pair import QuickSightAssetBundleImportJobDataSourceCredentialPair


class QuickSightAssetBundleImportJobDataSourceCredentials(BaseModel):
    CredentialPair: QuickSightAssetBundleImportJobDataSourceCredentialPair | None = None
    SecretArn: StrictStr | None = None
