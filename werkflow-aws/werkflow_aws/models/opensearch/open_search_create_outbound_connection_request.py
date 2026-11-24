from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .open_search_connection_properties import OpenSearchConnectionProperties
from .open_search_domain_information_container import OpenSearchDomainInformationContainer


class OpenSearchCreateOutboundConnectionRequest(BaseModel):
    LocalDomainInfo: OpenSearchDomainInformationContainer
    RemoteDomainInfo: OpenSearchDomainInformationContainer
    ConnectionAlias: StrictStr
    ConnectionMode: Literal['DIRECT', 'VPC_ENDPOINT'] | None = None
    ConnectionProperties: OpenSearchConnectionProperties | None = None
