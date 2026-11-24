from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .quick_sight_data_source_error_info import QuickSightDataSourceErrorInfo
from .quick_sight_data_source_parameters import QuickSightDataSourceParameters
from .quick_sight_ssl_properties import QuickSightSslProperties
from .quick_sight_vpc_connection_properties import QuickSightVpcConnectionProperties


class QuickSightDataSource(BaseModel):
    Arn: StrictStr | None = None
    DataSourceId: StrictStr | None = None
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    Status: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
    DataSourceParameters: QuickSightDataSourceParameters | None = None
    AlternateDataSourceParameters: list[QuickSightDataSourceParameters] | None = None
    VpcConnectionProperties: QuickSightVpcConnectionProperties | None = None
    SslProperties: QuickSightSslProperties | None = None
    ErrorInfo: QuickSightDataSourceErrorInfo | None = None
    SecretArn: StrictStr | None = None
    CredentialStatus: StrictStr | None = None
    LastCredentialVerifiedAt: datetime.datetime | StrictStr | None = None
