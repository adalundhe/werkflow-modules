from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .msk_cluster_operation_v2_provisioned import MSKClusterOperationV2Provisioned
from .msk_cluster_operation_v2_serverless import MSKClusterOperationV2Serverless
from .msk_error_info import MSKErrorInfo


class MSKClusterOperationV2(BaseModel):
    ClusterArn: StrictStr | None = None
    ClusterType: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    ErrorInfo: MSKErrorInfo | None = None
    OperationArn: StrictStr | None = None
    OperationState: StrictStr | None = None
    OperationType: StrictStr | None = None
    Provisioned: MSKClusterOperationV2Provisioned | None = None
    Serverless: MSKClusterOperationV2Serverless | None = None
