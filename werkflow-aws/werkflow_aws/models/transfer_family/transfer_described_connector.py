from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .transfer_as2_connector_config import TransferAs2ConnectorConfig
from .transfer_described_connector_egress_config import TransferDescribedConnectorEgressConfig
from .transfer_sftp_connector_config import TransferSftpConnectorConfig
from .transfer_tag import TransferTag


class TransferDescribedConnector(BaseModel):
    Arn: StrictStr | None = None
    ConnectorId: StrictStr | None = None
    Url: StrictStr | None = None
    As2Config: TransferAs2ConnectorConfig | None = None
    AccessRole: StrictStr | None = None
    LoggingRole: StrictStr | None = None
    Tags: list[TransferTag] | None = None
    SftpConfig: TransferSftpConnectorConfig | None = None
    ServiceManagedEgressIpAddresses: list[StrictStr] | None = None
    SecurityPolicyName: StrictStr | None = None
    EgressConfig: TransferDescribedConnectorEgressConfig | None = None
    EgressType: StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    Status: StrictStr | None = None
    IpAddressType: StrictStr | None = None
