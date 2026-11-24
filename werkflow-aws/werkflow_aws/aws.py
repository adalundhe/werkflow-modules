from __future__ import annotations

import importlib
from typing import TYPE_CHECKING, Any, cast

from werkflow_core import Module
from werkflow_aws.models import (
    AWSCredentialsSet,
    RegionName,
)
from werkflow_aws.models.sts import AssumeRoleRequest
from .authorization_type import AuthorizationType
from .parsers import AWSConfigParser
from .services.aws_credentials import AWSCredentials
from .supported_clients import SupportedClients

if TYPE_CHECKING:
    from .services import (
        AWSAthena,
        AWSBaseService,
        AWSCloudwatch,
        AWSCodeArtifact,
        AWSCostExplorer,
        AWSDynamoDB,
        AWSEC2,
        AWSEKS,
        AWSElasticBlockStorage,
        AWSElastiCache,
        AWSIAM,
        AWSLambda,
        AWSMSK,
        AWSOrganizations,
        AWSRDS,
        AWSRoute53,
        AWSs3,
        AWSSageMaker,
        AWSSecretsManager,
        AWSSQS,
        AWSSTS,
    )

_CLIENT_FACTORY_MAP: dict[SupportedClients, tuple[str, str]] = {
    "athena": ("werkflow_aws.services.aws_athena", "AWSAthena"),
    "cloudwatch": ("werkflow_aws.services.aws_cloudwatch", "AWSCloudwatch"),
    "code-artifact": ("werkflow_aws.services.aws_codeartifact", "AWSCodeArtifact"),
    "cost-explorer": ("werkflow_aws.services.aws_cost_explorer", "AWSCostExplorer"),
    "dynamodb": ("werkflow_aws.services.aws_dynamodb", "AWSDynamoDB"),
    "ebs": ("werkflow_aws.services.aws_elastic_block_storage", "AWSElasticBlockStorage"),
    "ec2": ("werkflow_aws.services.aws_ec2", "AWSEC2"),
    "eks": ("werkflow_aws.services.aws_eks", "AWSEKS"),
    "elasticache": ("werkflow_aws.services.aws_elasticache", "AWSElastiCache"),
    "iam": ("werkflow_aws.services.aws_iam", "AWSIAM"),
    "lambda": ("werkflow_aws.services.aws_lambda", "AWSLambda"),
    "msk": ("werkflow_aws.services.aws_msk", "AWSMSK"),
    "organizations": ("werkflow_aws.services.aws_organizations", "AWSOrganizations"),
    "rds": ("werkflow_aws.services.aws_rds", "AWSRDS"),
    "route53": ("werkflow_aws.services.aws_route53", "AWSRoute53"),
    "s3": ("werkflow_aws.services.aws_s3", "AWSs3"),
    "sagemaker": ("werkflow_aws.services.aws_sagemaker", "AWSSageMaker"),
    "secrets-manager": ("werkflow_aws.services.aws_secrets_manager", "AWSSecretsManager"),
    "sqs": ("werkflow_aws.services.aws_sqs", "AWSSQS"),
    "sts": ("werkflow_aws.services.aws_sts", "AWSSTS"),
}


class AWS(Module):
    dependencies = [
        'boto3',
        'pydantic',
        'werkflow-secrets',
        'werkflow-shell',
        'werkflow-system',
    ]

    def __init__(self) -> None:
        super().__init__()
        self.config = AWSConfigParser()
        self.credentials = AWSCredentials()
        self._clients: dict[SupportedClients, AWSBaseService[Any]] = {}

    def _get_service(self, client: SupportedClients) -> AWSBaseService[Any]:
        service = self._clients.get(client)
        if service is not None:
            return service

        factory = _CLIENT_FACTORY_MAP.get(client)
        if factory is None:
            supported = ', '.join(sorted(_CLIENT_FACTORY_MAP.keys()))
            raise ValueError(
                f"Unsupported AWS client '{client}'. Supported clients: {supported}"
            )
        module_name, class_name = factory
        module = importlib.import_module(module_name)
        service_cls = getattr(module, class_name)
        instance: AWSBaseService[Any] = service_cls()
        self._clients[client] = instance
        return instance

    @property
    def athena(self) -> AWSAthena:
        return cast('AWSAthena', self._get_service('athena'))

    @property
    def cloudwatch(self) -> AWSCloudwatch:
        return cast('AWSCloudwatch', self._get_service('cloudwatch'))

    @property
    def code_artifact(self) -> AWSCodeArtifact:
        return cast('AWSCodeArtifact', self._get_service('code-artifact'))

    @property
    def cost_explorer(self) -> AWSCostExplorer:
        return cast('AWSCostExplorer', self._get_service('cost-explorer'))

    @property
    def dynamodb(self) -> AWSDynamoDB:
        return cast('AWSDynamoDB', self._get_service('dynamodb'))

    @property
    def ebs(self) -> AWSElasticBlockStorage:
        return cast('AWSElasticBlockStorage', self._get_service('ebs'))

    @property
    def ec2(self) -> AWSEC2:
        return cast('AWSEC2', self._get_service('ec2'))

    @property
    def eks(self) -> AWSEKS:
        return cast('AWSEKS', self._get_service('eks'))

    @property
    def elasticache(self) -> AWSElastiCache:
        return cast('AWSElastiCache', self._get_service('elasticache'))

    @property
    def iam(self) -> AWSIAM:
        return cast('AWSIAM', self._get_service('iam'))

    @property
    def aws_lambda(self) -> AWSLambda:
        return cast('AWSLambda', self._get_service('lambda'))

    @property
    def lambda_(self) -> AWSLambda:
        return self.aws_lambda

    @property
    def msk(self) -> AWSMSK:
        return cast('AWSMSK', self._get_service('msk'))

    @property
    def organizations(self) -> AWSOrganizations:
        return cast('AWSOrganizations', self._get_service('organizations'))

    @property
    def rds(self) -> AWSRDS:
        return cast('AWSRDS', self._get_service('rds'))

    @property
    def route53(self) -> AWSRoute53:
        return cast('AWSRoute53', self._get_service('route53'))

    @property
    def s3(self) -> AWSs3:
        return cast('AWSs3', self._get_service('s3'))

    @property
    def sagemaker(self) -> AWSSageMaker:
        return cast('AWSSageMaker', self._get_service('sagemaker'))

    @property
    def secrets_manager(self) -> AWSSecretsManager:
        return cast('AWSSecretsManager', self._get_service('secrets-manager'))

    @property
    def sqs(self) -> AWSSQS:
        return cast('AWSSQS', self._get_service('sqs'))

    @property
    def sts(self) -> AWSSTS:
        return cast('AWSSTS', self._get_service('sts'))

    async def connect(
        self,
        client: SupportedClients,
        credentials: AWSCredentialsSet | None = None,
        region: RegionName = 'us-east-1',
        authorization_type: AuthorizationType = "client",
        assume_role_request: AssumeRoleRequest | None = None,
        assume_proxy_role_request: AssumeRoleRequest | None = None,
    ) -> None:
        match authorization_type:
            case "assume":
                if assume_role_request is None:
                    raise ValueError(
                        "assume_role_request is required when authorization_type='assume'."
                    )
                await self._connect_assumed_role(
                    client=client,
                    assume_role_request=assume_role_request,
                    assume_proxy_role_request=assume_proxy_role_request,
                    region=region,
                    credentials=credentials,
                )
            case "sso":
                if credentials is None or not credentials.aws_profile:
                    raise ValueError(
                        "credentials with aws_profile set is required when authorization_type='sso'."
                    )
                await self._connect_sso(
                    client=client,
                    credentials=credentials,
                    region=region,
                )
            case "client":
                await self._connect_client(
                    client=client,
                    credentials=credentials,
                    region=region,
                )
            case _:
                raise ValueError(
                    f"Unsupported authorization_type '{authorization_type}'. "
                    "Expected 'client', 'sso', or 'assume'."
                )

    async def _connect_assumed_role(
        self,
        client: SupportedClients,
        assume_role_request: AssumeRoleRequest,
        assume_proxy_role_request: AssumeRoleRequest | None,
        region: RegionName,
        credentials: AWSCredentialsSet | None = None,
    ) -> None:
        if self.sts._client is None:
            await self.sts.connect(region=region, credentials=credentials)

        if assume_proxy_role_request is not None:
            response = await self.sts.assume_role_by_proxy(
                assume_role_request,
                assume_proxy_role_request,
                region,
            )
        else:
            response = await self.sts.assume_role(assume_role_request)

        if response.Credentials is None:
            raise RuntimeError('STS assume_role returned no credentials.')

        await self._connect_client(
            client=client,
            credentials=AWSCredentialsSet(
                aws_access_key_id=response.Credentials.AccessKeyId,
                aws_secret_access_key=response.Credentials.SecretAccessKey,
                aws_session_token=response.Credentials.SessionToken,
            ),
            region=region,
        )

    async def _connect_sso(
        self,
        client: SupportedClients,
        credentials: AWSCredentialsSet,
        region: RegionName | None = None,
    ) -> None:
        if not credentials.aws_profile:
            raise ValueError("credentials.aws_profile must be set for SSO connections.")
        service = self._get_service(client)
        await service.sso(credentials.aws_profile, region=region)

    async def _connect_client(
        self,
        client: SupportedClients,
        credentials: AWSCredentialsSet | None,
        region: RegionName,
    ) -> None:
        service = self._get_service(client)
        await service.connect(region=region, credentials=credentials)

    async def close(self) -> None:
        for service in list(self._clients.values()):
            await service.close()
        self._clients.clear()
        await self.credentials.close()
        await self.config.close()

    def abort(self) -> None:
        for service in list(self._clients.values()):
            service.abort()
        self._clients.clear()
        self.credentials.abort()
        self.config.abort()
