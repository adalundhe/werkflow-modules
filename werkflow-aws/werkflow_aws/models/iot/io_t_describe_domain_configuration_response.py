from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .io_t_authorizer_config import IoTAuthorizerConfig
from .io_t_client_certificate_config import IoTClientCertificateConfig
from .io_t_server_certificate_config import IoTServerCertificateConfig
from .io_t_server_certificate_summary import IoTServerCertificateSummary
from .io_t_tls_config import IoTTlsConfig


class IoTDescribeDomainConfigurationResponse(BaseModel):
    domainConfigurationName: StrictStr | None = None
    domainConfigurationArn: StrictStr | None = None
    domainName: StrictStr | None = None
    serverCertificates: list[IoTServerCertificateSummary] | None = None
    authorizerConfig: IoTAuthorizerConfig | None = None
    domainConfigurationStatus: StrictStr | None = None
    serviceType: StrictStr | None = None
    domainType: StrictStr | None = None
    lastStatusChangeDate: datetime.datetime | StrictStr | None = None
    tlsConfig: IoTTlsConfig | None = None
    serverCertificateConfig: IoTServerCertificateConfig | None = None
    authenticationType: StrictStr | None = None
    applicationProtocol: StrictStr | None = None
    clientCertificateConfig: IoTClientCertificateConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None
