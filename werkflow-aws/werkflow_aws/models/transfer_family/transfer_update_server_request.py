from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .transfer_endpoint_details import TransferEndpointDetails
from .transfer_identity_provider_details import TransferIdentityProviderDetails
from .transfer_protocol_details import TransferProtocolDetails
from .transfer_s3_storage_options import TransferS3StorageOptions
from .transfer_workflow_details import TransferWorkflowDetails


class TransferUpdateServerRequest(BaseModel):
    ServerId: StrictStr
    Certificate: StrictStr | None = None
    ProtocolDetails: TransferProtocolDetails | None = None
    EndpointDetails: TransferEndpointDetails | None = None
    EndpointType: Literal['PUBLIC', 'VPC', 'VPC_ENDPOINT'] | None = None
    HostKey: StrictStr | None = None
    IdentityProviderDetails: TransferIdentityProviderDetails | None = None
    LoggingRole: StrictStr | None = None
    PostAuthenticationLoginBanner: StrictStr | None = None
    PreAuthenticationLoginBanner: StrictStr | None = None
    Protocols: list[Literal['SFTP', 'FTP', 'FTPS', 'AS2']] | None = None
    SecurityPolicyName: StrictStr | None = None
    WorkflowDetails: TransferWorkflowDetails | None = None
    StructuredLogDestinations: list[StrictStr] | None = None
    S3StorageOptions: TransferS3StorageOptions | None = None
    IpAddressType: Literal['IPV4', 'DUALSTACK'] | None = None
    IdentityProviderType: Literal['SERVICE_MANAGED', 'API_GATEWAY', 'AWS_DIRECTORY_SERVICE', 'AWS_LAMBDA'] | None = None
