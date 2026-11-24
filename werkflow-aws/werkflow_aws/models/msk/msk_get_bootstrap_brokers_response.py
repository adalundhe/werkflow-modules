from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MSKGetBootstrapBrokersResponse(BaseModel):
    BootstrapBrokerString: StrictStr | None = None
    BootstrapBrokerStringTls: StrictStr | None = None
    BootstrapBrokerStringSaslScram: StrictStr | None = None
    BootstrapBrokerStringSaslIam: StrictStr | None = None
    BootstrapBrokerStringPublicTls: StrictStr | None = None
    BootstrapBrokerStringPublicSaslScram: StrictStr | None = None
    BootstrapBrokerStringPublicSaslIam: StrictStr | None = None
    BootstrapBrokerStringVpcConnectivityTls: StrictStr | None = None
    BootstrapBrokerStringVpcConnectivitySaslScram: StrictStr | None = None
    BootstrapBrokerStringVpcConnectivitySaslIam: StrictStr | None = None
