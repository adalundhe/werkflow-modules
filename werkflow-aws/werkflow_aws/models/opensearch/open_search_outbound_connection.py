from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .open_search_connection_properties import OpenSearchConnectionProperties
from .open_search_domain_information_container import OpenSearchDomainInformationContainer
from .open_search_outbound_connection_status import OpenSearchOutboundConnectionStatus


class OpenSearchOutboundConnection(BaseModel):
    LocalDomainInfo: OpenSearchDomainInformationContainer | None = None
    RemoteDomainInfo: OpenSearchDomainInformationContainer | None = None
    ConnectionId: StrictStr | None = None
    ConnectionAlias: StrictStr | None = None
    ConnectionStatus: OpenSearchOutboundConnectionStatus | None = None
    ConnectionMode: StrictStr | None = None
    ConnectionProperties: OpenSearchConnectionProperties | None = None
