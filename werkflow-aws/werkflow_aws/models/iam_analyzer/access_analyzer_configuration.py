from __future__ import annotations
from pydantic import BaseModel
from .access_analyzer_dynamodb_stream_configuration import AccessAnalyzerDynamodbStreamConfiguration
from .access_analyzer_dynamodb_table_configuration import AccessAnalyzerDynamodbTableConfiguration
from .access_analyzer_ebs_snapshot_configuration import AccessAnalyzerEbsSnapshotConfiguration
from .access_analyzer_ecr_repository_configuration import AccessAnalyzerEcrRepositoryConfiguration
from .access_analyzer_efs_file_system_configuration import AccessAnalyzerEfsFileSystemConfiguration
from .access_analyzer_iam_role_configuration import AccessAnalyzerIamRoleConfiguration
from .access_analyzer_kms_key_configuration import AccessAnalyzerKmsKeyConfiguration
from .access_analyzer_rds_db_cluster_snapshot_configuration import AccessAnalyzerRdsDbClusterSnapshotConfiguration
from .access_analyzer_rds_db_snapshot_configuration import AccessAnalyzerRdsDbSnapshotConfiguration
from .access_analyzer_s3_bucket_configuration import AccessAnalyzerS3BucketConfiguration
from .access_analyzer_s3_express_directory_bucket_configuration import AccessAnalyzerS3ExpressDirectoryBucketConfiguration
from .access_analyzer_secrets_manager_secret_configuration import AccessAnalyzerSecretsManagerSecretConfiguration
from .access_analyzer_sns_topic_configuration import AccessAnalyzerSnsTopicConfiguration
from .access_analyzer_sqs_queue_configuration import AccessAnalyzerSqsQueueConfiguration


class AccessAnalyzerConfiguration(BaseModel):
    ebsSnapshot: AccessAnalyzerEbsSnapshotConfiguration | None = None
    ecrRepository: AccessAnalyzerEcrRepositoryConfiguration | None = None
    iamRole: AccessAnalyzerIamRoleConfiguration | None = None
    efsFileSystem: AccessAnalyzerEfsFileSystemConfiguration | None = None
    kmsKey: AccessAnalyzerKmsKeyConfiguration | None = None
    rdsDbClusterSnapshot: AccessAnalyzerRdsDbClusterSnapshotConfiguration | None = None
    rdsDbSnapshot: AccessAnalyzerRdsDbSnapshotConfiguration | None = None
    secretsManagerSecret: AccessAnalyzerSecretsManagerSecretConfiguration | None = None
    s3Bucket: AccessAnalyzerS3BucketConfiguration | None = None
    snsTopic: AccessAnalyzerSnsTopicConfiguration | None = None
    sqsQueue: AccessAnalyzerSqsQueueConfiguration | None = None
    s3ExpressDirectoryBucket: AccessAnalyzerS3ExpressDirectoryBucketConfiguration | None = None
    dynamodbStream: AccessAnalyzerDynamodbStreamConfiguration | None = None
    dynamodbTable: AccessAnalyzerDynamodbTableConfiguration | None = None
