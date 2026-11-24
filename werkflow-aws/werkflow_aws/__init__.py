from __future__ import annotations

import importlib
from typing import TYPE_CHECKING, Any

from .authorization_type import AuthorizationType as AuthorizationType
from .aws import AWS as AWS
from .exceptions import (
    EmptyResponseException as EmptyResponseException,
    UnsetAWSConnectionException as UnsetAWSConnectionException,
)
from .models import (
    AWSCredentialsSet as AWSCredentialsSet,
    AWSRegion as AWSRegion,
    AWSRegionMap as AWSRegionMap,
    AWSServices as AWSServices,
    AWSServicesMap as AWSServicesMap,
    MappedServiceNames as MappedServiceNames,
    RegionName as RegionName,
    ServiceName as ServiceName,
)
from .parsers import AWSConfigParser as AWSConfigParser
from .services.aws_credentials import AWSCredentials as AWSCredentials
from .services.base import AWSBaseService as AWSBaseService
from .supported_clients import SupportedClients as SupportedClients

if TYPE_CHECKING:
    from .services import (
        AWSAthena as AWSAthena,
        AWSCloudwatch as AWSCloudwatch,
        AWSCodeArtifact as AWSCodeArtifact,
        AWSCostExplorer as AWSCostExplorer,
        AWSDynamoDB as AWSDynamoDB,
        AWSEC2 as AWSEC2,
        AWSEKS as AWSEKS,
        AWSElasticBlockStorage as AWSElasticBlockStorage,
        AWSElastiCache as AWSElastiCache,
        AWSIAM as AWSIAM,
        AWSLambda as AWSLambda,
        AWSMSK as AWSMSK,
        AWSOrganizations as AWSOrganizations,
        AWSRDS as AWSRDS,
        AWSRoute53 as AWSRoute53,
        AWSs3 as AWSs3,
        AWSSageMaker as AWSSageMaker,
        AWSSecretsManager as AWSSecretsManager,
        AWSSQS as AWSSQS,
        AWSSTS as AWSSTS,
    )

_LAZY_SERVICE_EXPORTS: dict[str, tuple[str, str]] = {
    'AWSAthena': ('.services.aws_athena', 'AWSAthena'),
    'AWSCloudwatch': ('.services.aws_cloudwatch', 'AWSCloudwatch'),
    'AWSCodeArtifact': ('.services.aws_codeartifact', 'AWSCodeArtifact'),
    'AWSCostExplorer': ('.services.aws_cost_explorer', 'AWSCostExplorer'),
    'AWSDynamoDB': ('.services.aws_dynamodb', 'AWSDynamoDB'),
    'AWSEC2': ('.services.aws_ec2', 'AWSEC2'),
    'AWSEKS': ('.services.aws_eks', 'AWSEKS'),
    'AWSElasticBlockStorage': ('.services.aws_elastic_block_storage', 'AWSElasticBlockStorage'),
    'AWSElastiCache': ('.services.aws_elasticache', 'AWSElastiCache'),
    'AWSIAM': ('.services.aws_iam', 'AWSIAM'),
    'AWSLambda': ('.services.aws_lambda', 'AWSLambda'),
    'AWSMSK': ('.services.aws_msk', 'AWSMSK'),
    'AWSOrganizations': ('.services.aws_organizations', 'AWSOrganizations'),
    'AWSRDS': ('.services.aws_rds', 'AWSRDS'),
    'AWSRoute53': ('.services.aws_route53', 'AWSRoute53'),
    'AWSs3': ('.services.aws_s3', 'AWSs3'),
    'AWSSageMaker': ('.services.aws_sagemaker', 'AWSSageMaker'),
    'AWSSecretsManager': ('.services.aws_secrets_manager', 'AWSSecretsManager'),
    'AWSSQS': ('.services.aws_sqs', 'AWSSQS'),
    'AWSSTS': ('.services.aws_sts', 'AWSSTS'),
}


def __getattr__(name: str) -> Any:
    target = _LAZY_SERVICE_EXPORTS.get(name)
    if target is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    module_name, attr_name = target
    module = importlib.import_module(module_name, __name__)
    value = getattr(module, attr_name)
    globals()[name] = value
    return value
