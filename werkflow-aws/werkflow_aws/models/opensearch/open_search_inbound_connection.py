from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_domain_information_container import OpenSearchDomainInformationContainer
from .open_search_inbound_connection_status import OpenSearchInboundConnectionStatus


class OpenSearchInboundConnection(BaseModel):
    LocalDomainInfo: OpenSearchDomainInformationContainer | None = None
    RemoteDomainInfo: OpenSearchDomainInformationContainer | None = None
    ConnectionId: StrictStr | None = None
    ConnectionStatus: OpenSearchInboundConnectionStatus | None = None
    ConnectionMode: StrictStr | None = None
