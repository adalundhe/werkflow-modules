from werkflow_core import Module
from .parsers import AWSConfigParser
from .services import (
    AWSAthena,
    AWSCloudwatch,
    AWSCredentials,
    AWSCodeArtifact,
    AWSCostExplorer,
    AWSEC2,
    AWSElastiCache,
    AWSMSK,
    AWSOrganizations,
    AWSs3,
    AWSSecretsManager,
    AWSSTS,
)
from werkflow_aws.models import (
    AWSCredentialsSet,
    RegionName,
)
from werkflow_aws.models.sts import AssumeRoleRequest
from .authorization_type import AuthorizationType
from .supported_clients import SupportedClients

class AWS(Module):

    def __init__(self) -> None:
        super().__init__()

        self.athena = AWSAthena()
        self.cloudwatch = AWSCloudwatch()
        self.config = AWSConfigParser()
        self.credentials = AWSCredentials()
        self.code_artifact = AWSCodeArtifact()
        self.cost_explorer = AWSCostExplorer()
        self.ec2 = AWSEC2()
        self.elasticache = AWSElastiCache()
        self.msk = AWSMSK()
        self.organizations = AWSOrganizations()
        self.s3 = AWSs3()
        self.sts = AWSSTS()
        self.secrets_manager = AWSSecretsManager()

    async def connect(
        self,
        client: SupportedClients,
        credentials: AWSCredentialsSet, 
        region: RegionName,
        authorization_type: AuthorizationType = "client"
    ):
        match authorization_type:
            case "assume":
                pass
            case "sso":
                pass
            case _:
                await self._connect_client(
                    client,
                    credentials,
                    region,
                )
    
    async def _connect_assumed_role(
        self,
        client: SupportedClients,
        assume_role_request: AssumeRoleRequest,
        assume_proxy_role_request: AssumeRoleRequest,
        region: RegionName,
    ):
        response = await self.sts.assume_role_by_proxy(
            assume_role_request,
            assume_proxy_role_request,
            region,
        )

        await self._connect_client(
            client,
            AWSCredentialsSet(
                aws_access_key_id=response.Credentials.AccessKeyId,
                aws_secret_access_key=response.Credentials.SecretAccessKey,
                aws_session_token=response.Credentials.SessionToken,
            ),
            region,
        )

    async def _connect_sso(
        self,
        client: SupportedClients,
        credentials: AWSCredentialsSet, 
    ):
        match client:
            case "athena":
                await self.athena.sso(credentials.aws_profile)
            
            case "cloudwatch":
                await self.cloudwatch.sso(credentials.aws_profile)

            case "code_artifact":
                await self.code_artifact.sso(credentials.aws_profile)
            
            case "ec2":
                await self.code_artifact.sso(credentials.aws_profile)
            
            case "elasticache":
                await self.elasticache.sso(credentials.aws_profile)

            case "msk":
                await self.msk.sso(credentials.aws_profile)

            case "organizations":
                await self.organizations.sso(credentials.aws_profile)

            case "sts": 
                await self.organizations.sso(credentials.aws_profile)
                
    
    async def _connect_client(
        self,
        client: SupportedClients,
        credentials: AWSCredentialsSet, 
        region: RegionName,
    ):
        match client:
            case "athena":
                await self.athena.connect(credentials, region)
            
            case "cloudwatch":
                await self.cloudwatch.connect(credentials, region)

            case "code-artifact":
                await self.code_artifact.connect(credentials, region)

            case "cost-explorer":
                await self.cost_explorer.connect(credentials, region)
            
            case "ec2":
                await self.code_artifact.connect(credentials, region)
            
            case "elasticache":
                await self.elasticache.connect(credentials, region)

            case "msk":
                await self.msk.connect(credentials, region)

            case "organizations":
                await self.organizations.connect(credentials, region)

            case "s3":
                await self.s3.connect(credentials, region)

            case "secrets-manager":
                await self.secrets_manager.connect(credentials, region)

            case "sts": 
                await self.organizations.connect(credentials, region)
                
    
    async def close(self):
        await self.athena.close()
        await self.cloudwatch.close()
        await self.credentials.close()
        await self.code_artifact.close()
        await self.cost_explorer.close()
        await self.ec2.close()
        await self.elasticache.close()
        await self.msk.close()
        await self.organizations.close()
        await self.s3.close()
        await self.secrets_manager.close()
        await self.sts.close()

    def abort(self):
        self.athena.abort()
        self.cloudwatch.abort()
        self.credentials.abort()
        self.code_artifact.abort()
        self.cost_explorer.abort()
        self.ec2.abort()
        self.elasticache.abort()
        self.msk.abort()
        self.organizations.abort()
        self.s3.abort()
        self.secrets_manager.abort()
        self.sts.abort()

    

