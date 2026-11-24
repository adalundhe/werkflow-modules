from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_data_source_credentials import QuickSightDataSourceCredentials
from .quick_sight_data_source_parameters import QuickSightDataSourceParameters
from .quick_sight_ssl_properties import QuickSightSslProperties
from .quick_sight_vpc_connection_properties import QuickSightVpcConnectionProperties


class QuickSightUpdateDataSourceRequest(BaseModel):
    AwsAccountId: StrictStr
    DataSourceId: StrictStr
    Name: StrictStr
    DataSourceParameters: QuickSightDataSourceParameters | None = None
    Credentials: QuickSightDataSourceCredentials | None = None
    VpcConnectionProperties: QuickSightVpcConnectionProperties | None = None
    SslProperties: QuickSightSslProperties | None = None
