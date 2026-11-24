from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .transfer_proxy_config import TransferProxyConfig
from .transfer_sftp_port_with_options import TransferSftpPortWithOptions


class TransferProtocolDetails(BaseModel):
    PassiveIp: StrictStr | None = None
    TlsSessionResumptionMode: StrictStr | None = None
    SetStatOption: StrictStr | None = None
    SftpPorts: list[TransferSftpPortWithOptions] | None = None
    As2Transports: list[StrictStr] | None = None
    ProxyConfig: TransferProxyConfig | None = None
