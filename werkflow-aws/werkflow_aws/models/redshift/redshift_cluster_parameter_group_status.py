from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .redshift_cluster_parameter_status import RedshiftClusterParameterStatus


class RedshiftClusterParameterGroupStatus(BaseModel):
    ParameterGroupName: StrictStr | None = None
    ParameterApplyStatus: StrictStr | None = None
    ClusterParameterStatusList: list[RedshiftClusterParameterStatus] | None = None
