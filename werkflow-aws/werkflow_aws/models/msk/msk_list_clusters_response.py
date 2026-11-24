from pydantic import BaseModel, StrictStr
from .msk_cluster import MSKCluster


class MSKListClustersResponse(BaseModel):
    ClusterInfoList: list[MSKCluster] | None = None
    NextToken: StrictStr | None = None
    
