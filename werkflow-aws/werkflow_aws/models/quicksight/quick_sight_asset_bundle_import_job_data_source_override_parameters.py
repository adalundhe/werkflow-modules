from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_asset_bundle_import_job_data_source_credentials import QuickSightAssetBundleImportJobDataSourceCredentials
from .quick_sight_data_source_parameters import QuickSightDataSourceParameters
from .quick_sight_ssl_properties import QuickSightSslProperties
from .quick_sight_vpc_connection_properties import QuickSightVpcConnectionProperties


class QuickSightAssetBundleImportJobDataSourceOverrideParameters(BaseModel):
    DataSourceId: StrictStr | None = None
    Name: StrictStr | None = None
    DataSourceParameters: QuickSightDataSourceParameters | None = None
    VpcConnectionProperties: QuickSightVpcConnectionProperties | None = None
    SslProperties: QuickSightSslProperties | None = None
    Credentials: QuickSightAssetBundleImportJobDataSourceCredentials | None = None
