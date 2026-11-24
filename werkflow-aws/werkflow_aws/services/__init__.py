from __future__ import annotations

import importlib
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .aws_athena import AWSAthena as AWSAthena
    from .aws_cloudwatch import AWSCloudwatch as AWSCloudwatch
    from .aws_codeartifact import AWSCodeArtifact as AWSCodeArtifact
    from .aws_cost_explorer import AWSCostExplorer as AWSCostExplorer
    from .aws_credentials import AWSCredentials as AWSCredentials
    from .aws_dynamodb import AWSDynamoDB as AWSDynamoDB
    from .aws_ec2 import AWSEC2 as AWSEC2
    from .aws_eks import AWSEKS as AWSEKS
    from .aws_elastic_block_storage import (
        AWSElasticBlockStorage as AWSElasticBlockStorage,
    )
    from .aws_elasticache import AWSElastiCache as AWSElastiCache
    from .aws_iam import AWSIAM as AWSIAM
    from .aws_lambda import AWSLambda as AWSLambda
    from .aws_msk import AWSMSK as AWSMSK
    from .aws_organizations import AWSOrganizations as AWSOrganizations
    from .aws_rds import AWSRDS as AWSRDS
    from .aws_route53 import AWSRoute53 as AWSRoute53
    from .aws_s3 import AWSs3 as AWSs3
    from .aws_sagemaker import AWSSageMaker as AWSSageMaker
    from .aws_secrets_manager import AWSSecretsManager as AWSSecretsManager
    from .aws_sqs import AWSSQS as AWSSQS
    from .aws_sts import AWSSTS as AWSSTS
    from .base import AWSBaseService as AWSBaseService

_SERVICE_EXPORTS: dict[str, tuple[str, str]] = {
    'AWSAthena': ('.aws_athena', 'AWSAthena'),
    'AWSBaseService': ('.base', 'AWSBaseService'),
    'AWSCloudwatch': ('.aws_cloudwatch', 'AWSCloudwatch'),
    'AWSCodeArtifact': ('.aws_codeartifact', 'AWSCodeArtifact'),
    'AWSCostExplorer': ('.aws_cost_explorer', 'AWSCostExplorer'),
    'AWSCredentials': ('.aws_credentials', 'AWSCredentials'),
    'AWSDynamoDB': ('.aws_dynamodb', 'AWSDynamoDB'),
    'AWSEC2': ('.aws_ec2', 'AWSEC2'),
    'AWSEKS': ('.aws_eks', 'AWSEKS'),
    'AWSElasticBlockStorage': ('.aws_elastic_block_storage', 'AWSElasticBlockStorage'),
    'AWSElastiCache': ('.aws_elasticache', 'AWSElastiCache'),
    'AWSIAM': ('.aws_iam', 'AWSIAM'),
    'AWSLambda': ('.aws_lambda', 'AWSLambda'),
    'AWSMSK': ('.aws_msk', 'AWSMSK'),
    'AWSOrganizations': ('.aws_organizations', 'AWSOrganizations'),
    'AWSRDS': ('.aws_rds', 'AWSRDS'),
    'AWSRoute53': ('.aws_route53', 'AWSRoute53'),
    'AWSs3': ('.aws_s3', 'AWSs3'),
    'AWSSageMaker': ('.aws_sagemaker', 'AWSSageMaker'),
    'AWSSecretsManager': ('.aws_secrets_manager', 'AWSSecretsManager'),
    'AWSSQS': ('.aws_sqs', 'AWSSQS'),
    'AWSSTS': ('.aws_sts', 'AWSSTS'),
}

__all__ = sorted(_SERVICE_EXPORTS.keys())


def __getattr__(name: str) -> Any:
    target = _SERVICE_EXPORTS.get(name)
    if target is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    module_name, attr_name = target
    module = importlib.import_module(module_name, __name__)
    value = getattr(module, attr_name)
    globals()[name] = value
    return value
