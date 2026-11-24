from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .io_t_authorizer_config import IoTAuthorizerConfig
from .io_t_client_certificate_config import IoTClientCertificateConfig
from .io_t_server_certificate_config import IoTServerCertificateConfig
from .io_t_tls_config import IoTTlsConfig


class IoTUpdateDomainConfigurationRequest(BaseModel):
    domainConfigurationName: StrictStr
    authorizerConfig: IoTAuthorizerConfig | None = None
    domainConfigurationStatus: Literal['ENABLED', 'DISABLED'] | None = None
    removeAuthorizerConfig: StrictBool | None = None
    tlsConfig: IoTTlsConfig | None = None
    serverCertificateConfig: IoTServerCertificateConfig | None = None
    authenticationType: Literal['CUSTOM_AUTH_X509', 'CUSTOM_AUTH', 'AWS_X509', 'AWS_SIGV4', 'DEFAULT'] | None = None
    applicationProtocol: Literal['SECURE_MQTT', 'MQTT_WSS', 'HTTPS', 'DEFAULT'] | None = None
    clientCertificateConfig: IoTClientCertificateConfig | None = None
