from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_sync_tag_list_entry import DataSyncTagListEntry


class DataSyncCreateAgentRequest(BaseModel):
    ActivationKey: StrictStr
    AgentName: StrictStr | None = None
    Tags: list[DataSyncTagListEntry] | None = None
    VpcEndpointId: StrictStr | None = None
    SubnetArns: list[StrictStr] | None = None
    SecurityGroupArns: list[StrictStr] | None = None
