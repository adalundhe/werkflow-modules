from pydantic import BaseModel, StrictStr
from .msk_broker_node_group_info import MSKBrokerNodeGroupInfo


class MSKListClustersResponse(BaseModel):
    ClusterInfoList: list[MSKBrokerNodeGroupInfo]
    NextToken: StrictStr | None = None
    