from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .transfer_as2_connector_config import TransferAs2ConnectorConfig
from .transfer_connector_egress_config import TransferConnectorEgressConfig
from .transfer_sftp_connector_config import TransferSftpConnectorConfig
from .transfer_tag import TransferTag


class TransferCreateConnectorRequest(BaseModel):
    AccessRole: StrictStr
    Url: StrictStr | None = None
    As2Config: TransferAs2ConnectorConfig | None = None
    LoggingRole: StrictStr | None = None
    Tags: list[TransferTag] | None = None
    SftpConfig: TransferSftpConnectorConfig | None = None
    SecurityPolicyName: StrictStr | None = None
    EgressConfig: TransferConnectorEgressConfig | None = None
    IpAddressType: Literal['IPV4', 'DUALSTACK'] | None = None
