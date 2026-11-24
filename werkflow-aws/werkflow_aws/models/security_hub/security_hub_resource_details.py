from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .security_hub_aws_amazon_mq_broker_details import SecurityHubAwsAmazonMqBrokerDetails
from .security_hub_aws_api_gateway_rest_api_details import SecurityHubAwsApiGatewayRestApiDetails
from .security_hub_aws_api_gateway_stage_details import SecurityHubAwsApiGatewayStageDetails
from .security_hub_aws_api_gateway_v2_api_details import SecurityHubAwsApiGatewayV2ApiDetails
from .security_hub_aws_api_gateway_v2_stage_details import SecurityHubAwsApiGatewayV2StageDetails
from .security_hub_aws_app_sync_graph_ql_api_details import SecurityHubAwsAppSyncGraphQlApiDetails
from .security_hub_aws_athena_work_group_details import SecurityHubAwsAthenaWorkGroupDetails
from .security_hub_aws_auto_scaling_auto_scaling_group_details import SecurityHubAwsAutoScalingAutoScalingGroupDetails
from .security_hub_aws_auto_scaling_launch_configuration_details import SecurityHubAwsAutoScalingLaunchConfigurationDetails
from .security_hub_aws_backup_backup_plan_details import SecurityHubAwsBackupBackupPlanDetails
from .security_hub_aws_backup_backup_vault_details import SecurityHubAwsBackupBackupVaultDetails
from .security_hub_aws_backup_recovery_point_details import SecurityHubAwsBackupRecoveryPointDetails
from .security_hub_aws_certificate_manager_certificate_details import SecurityHubAwsCertificateManagerCertificateDetails
from .security_hub_aws_cloud_formation_stack_details import SecurityHubAwsCloudFormationStackDetails
from .security_hub_aws_cloud_front_distribution_details import SecurityHubAwsCloudFrontDistributionDetails
from .security_hub_aws_cloud_trail_trail_details import SecurityHubAwsCloudTrailTrailDetails
from .security_hub_aws_cloud_watch_alarm_details import SecurityHubAwsCloudWatchAlarmDetails
from .security_hub_aws_code_build_project_details import SecurityHubAwsCodeBuildProjectDetails
from .security_hub_aws_dms_endpoint_details import SecurityHubAwsDmsEndpointDetails
from .security_hub_aws_dms_replication_instance_details import SecurityHubAwsDmsReplicationInstanceDetails
from .security_hub_aws_dms_replication_task_details import SecurityHubAwsDmsReplicationTaskDetails
from .security_hub_aws_dynamo_db_table_details import SecurityHubAwsDynamoDbTableDetails
from .security_hub_aws_ec2_client_vpn_endpoint_details import SecurityHubAwsEc2ClientVpnEndpointDetails
from .security_hub_aws_ec2_eip_details import SecurityHubAwsEc2EipDetails
from .security_hub_aws_ec2_instance_details import SecurityHubAwsEc2InstanceDetails
from .security_hub_aws_ec2_launch_template_details import SecurityHubAwsEc2LaunchTemplateDetails
from .security_hub_aws_ec2_network_acl_details import SecurityHubAwsEc2NetworkAclDetails
from .security_hub_aws_ec2_network_interface_details import SecurityHubAwsEc2NetworkInterfaceDetails
from .security_hub_aws_ec2_route_table_details import SecurityHubAwsEc2RouteTableDetails
from .security_hub_aws_ec2_security_group_details import SecurityHubAwsEc2SecurityGroupDetails
from .security_hub_aws_ec2_subnet_details import SecurityHubAwsEc2SubnetDetails
from .security_hub_aws_ec2_transit_gateway_details import SecurityHubAwsEc2TransitGatewayDetails
from .security_hub_aws_ec2_volume_details import SecurityHubAwsEc2VolumeDetails
from .security_hub_aws_ec2_vpc_details import SecurityHubAwsEc2VpcDetails
from .security_hub_aws_ec2_vpc_endpoint_service_details import SecurityHubAwsEc2VpcEndpointServiceDetails
from .security_hub_aws_ec2_vpc_peering_connection_details import SecurityHubAwsEc2VpcPeeringConnectionDetails
from .security_hub_aws_ec2_vpn_connection_details import SecurityHubAwsEc2VpnConnectionDetails
from .security_hub_aws_ecr_container_image_details import SecurityHubAwsEcrContainerImageDetails
from .security_hub_aws_ecr_repository_details import SecurityHubAwsEcrRepositoryDetails
from .security_hub_aws_ecs_cluster_details import SecurityHubAwsEcsClusterDetails
from .security_hub_aws_ecs_container_details import SecurityHubAwsEcsContainerDetails
from .security_hub_aws_ecs_service_details import SecurityHubAwsEcsServiceDetails
from .security_hub_aws_ecs_task_definition_details import SecurityHubAwsEcsTaskDefinitionDetails
from .security_hub_aws_ecs_task_details import SecurityHubAwsEcsTaskDetails
from .security_hub_aws_efs_access_point_details import SecurityHubAwsEfsAccessPointDetails
from .security_hub_aws_eks_cluster_details import SecurityHubAwsEksClusterDetails
from .security_hub_aws_elastic_beanstalk_environment_details import SecurityHubAwsElasticBeanstalkEnvironmentDetails
from .security_hub_aws_elasticsearch_domain_details import SecurityHubAwsElasticsearchDomainDetails
from .security_hub_aws_elb_load_balancer_details import SecurityHubAwsElbLoadBalancerDetails
from .security_hub_aws_elbv2_load_balancer_details import SecurityHubAwsElbv2LoadBalancerDetails
from .security_hub_aws_event_schemas_registry_details import SecurityHubAwsEventSchemasRegistryDetails
from .security_hub_aws_events_endpoint_details import SecurityHubAwsEventsEndpointDetails
from .security_hub_aws_events_eventbus_details import SecurityHubAwsEventsEventbusDetails
from .security_hub_aws_guard_duty_detector_details import SecurityHubAwsGuardDutyDetectorDetails
from .security_hub_aws_iam_access_key_details import SecurityHubAwsIamAccessKeyDetails
from .security_hub_aws_iam_group_details import SecurityHubAwsIamGroupDetails
from .security_hub_aws_iam_policy_details import SecurityHubAwsIamPolicyDetails
from .security_hub_aws_iam_role_details import SecurityHubAwsIamRoleDetails
from .security_hub_aws_iam_user_details import SecurityHubAwsIamUserDetails
from .security_hub_aws_kinesis_stream_details import SecurityHubAwsKinesisStreamDetails
from .security_hub_aws_kms_key_details import SecurityHubAwsKmsKeyDetails
from .security_hub_aws_lambda_function_details import SecurityHubAwsLambdaFunctionDetails
from .security_hub_aws_lambda_layer_version_details import SecurityHubAwsLambdaLayerVersionDetails
from .security_hub_aws_msk_cluster_details import SecurityHubAwsMskClusterDetails
from .security_hub_aws_network_firewall_firewall_details import SecurityHubAwsNetworkFirewallFirewallDetails
from .security_hub_aws_network_firewall_firewall_policy_details import SecurityHubAwsNetworkFirewallFirewallPolicyDetails
from .security_hub_aws_network_firewall_rule_group_details import SecurityHubAwsNetworkFirewallRuleGroupDetails
from .security_hub_aws_open_search_service_domain_details import SecurityHubAwsOpenSearchServiceDomainDetails
from .security_hub_aws_rds_db_cluster_details import SecurityHubAwsRdsDbClusterDetails
from .security_hub_aws_rds_db_cluster_snapshot_details import SecurityHubAwsRdsDbClusterSnapshotDetails
from .security_hub_aws_rds_db_instance_details import SecurityHubAwsRdsDbInstanceDetails
from .security_hub_aws_rds_db_security_group_details import SecurityHubAwsRdsDbSecurityGroupDetails
from .security_hub_aws_rds_db_snapshot_details import SecurityHubAwsRdsDbSnapshotDetails
from .security_hub_aws_rds_event_subscription_details import SecurityHubAwsRdsEventSubscriptionDetails
from .security_hub_aws_redshift_cluster_details import SecurityHubAwsRedshiftClusterDetails
from .security_hub_aws_route53_hosted_zone_details import SecurityHubAwsRoute53HostedZoneDetails
from .security_hub_aws_s3_access_point_details import SecurityHubAwsS3AccessPointDetails
from .security_hub_aws_s3_account_public_access_block_details import SecurityHubAwsS3AccountPublicAccessBlockDetails
from .security_hub_aws_s3_bucket_details import SecurityHubAwsS3BucketDetails
from .security_hub_aws_s3_object_details import SecurityHubAwsS3ObjectDetails
from .security_hub_aws_sage_maker_notebook_instance_details import SecurityHubAwsSageMakerNotebookInstanceDetails
from .security_hub_aws_secrets_manager_secret_details import SecurityHubAwsSecretsManagerSecretDetails
from .security_hub_aws_sns_topic_details import SecurityHubAwsSnsTopicDetails
from .security_hub_aws_sqs_queue_details import SecurityHubAwsSqsQueueDetails
from .security_hub_aws_ssm_patch_compliance_details import SecurityHubAwsSsmPatchComplianceDetails
from .security_hub_aws_step_function_state_machine_details import SecurityHubAwsStepFunctionStateMachineDetails
from .security_hub_aws_waf_rate_based_rule_details import SecurityHubAwsWafRateBasedRuleDetails
from .security_hub_aws_waf_regional_rate_based_rule_details import SecurityHubAwsWafRegionalRateBasedRuleDetails
from .security_hub_aws_waf_regional_rule_details import SecurityHubAwsWafRegionalRuleDetails
from .security_hub_aws_waf_regional_rule_group_details import SecurityHubAwsWafRegionalRuleGroupDetails
from .security_hub_aws_waf_regional_web_acl_details import SecurityHubAwsWafRegionalWebAclDetails
from .security_hub_aws_waf_rule_details import SecurityHubAwsWafRuleDetails
from .security_hub_aws_waf_rule_group_details import SecurityHubAwsWafRuleGroupDetails
from .security_hub_aws_waf_web_acl_details import SecurityHubAwsWafWebAclDetails
from .security_hub_aws_wafv2_rule_group_details import SecurityHubAwsWafv2RuleGroupDetails
from .security_hub_aws_wafv2_web_acl_details import SecurityHubAwsWafv2WebAclDetails
from .security_hub_aws_xray_encryption_config_details import SecurityHubAwsXrayEncryptionConfigDetails
from .security_hub_azure_resource_details import SecurityHubAzureResourceDetails
from .security_hub_code_repository_details import SecurityHubCodeRepositoryDetails
from .security_hub_container_details import SecurityHubContainerDetails
from .security_hub_gcp_resource_details import SecurityHubGcpResourceDetails


class SecurityHubResourceDetails(BaseModel):
    AwsAutoScalingAutoScalingGroup: SecurityHubAwsAutoScalingAutoScalingGroupDetails | None = None
    AwsCodeBuildProject: SecurityHubAwsCodeBuildProjectDetails | None = None
    AwsCloudFrontDistribution: SecurityHubAwsCloudFrontDistributionDetails | None = None
    AwsEc2Instance: SecurityHubAwsEc2InstanceDetails | None = None
    AwsEc2NetworkInterface: SecurityHubAwsEc2NetworkInterfaceDetails | None = None
    AwsEc2SecurityGroup: SecurityHubAwsEc2SecurityGroupDetails | None = None
    AwsEc2Volume: SecurityHubAwsEc2VolumeDetails | None = None
    AwsEc2Vpc: SecurityHubAwsEc2VpcDetails | None = None
    AwsEc2Eip: SecurityHubAwsEc2EipDetails | None = None
    AwsEc2Subnet: SecurityHubAwsEc2SubnetDetails | None = None
    AwsEc2NetworkAcl: SecurityHubAwsEc2NetworkAclDetails | None = None
    AwsElbv2LoadBalancer: SecurityHubAwsElbv2LoadBalancerDetails | None = None
    AwsElasticBeanstalkEnvironment: SecurityHubAwsElasticBeanstalkEnvironmentDetails | None = None
    AwsElasticsearchDomain: SecurityHubAwsElasticsearchDomainDetails | None = None
    AwsS3Bucket: SecurityHubAwsS3BucketDetails | None = None
    AwsS3AccountPublicAccessBlock: SecurityHubAwsS3AccountPublicAccessBlockDetails | None = None
    AwsS3Object: SecurityHubAwsS3ObjectDetails | None = None
    AwsSecretsManagerSecret: SecurityHubAwsSecretsManagerSecretDetails | None = None
    AwsIamAccessKey: SecurityHubAwsIamAccessKeyDetails | None = None
    AwsIamUser: SecurityHubAwsIamUserDetails | None = None
    AwsIamPolicy: SecurityHubAwsIamPolicyDetails | None = None
    AwsApiGatewayV2Stage: SecurityHubAwsApiGatewayV2StageDetails | None = None
    AwsApiGatewayV2Api: SecurityHubAwsApiGatewayV2ApiDetails | None = None
    AwsDynamoDbTable: SecurityHubAwsDynamoDbTableDetails | None = None
    AwsApiGatewayStage: SecurityHubAwsApiGatewayStageDetails | None = None
    AwsApiGatewayRestApi: SecurityHubAwsApiGatewayRestApiDetails | None = None
    AwsCloudTrailTrail: SecurityHubAwsCloudTrailTrailDetails | None = None
    AwsSsmPatchCompliance: SecurityHubAwsSsmPatchComplianceDetails | None = None
    AwsCertificateManagerCertificate: SecurityHubAwsCertificateManagerCertificateDetails | None = None
    AwsRedshiftCluster: SecurityHubAwsRedshiftClusterDetails | None = None
    AwsElbLoadBalancer: SecurityHubAwsElbLoadBalancerDetails | None = None
    AwsIamGroup: SecurityHubAwsIamGroupDetails | None = None
    AwsIamRole: SecurityHubAwsIamRoleDetails | None = None
    AwsKmsKey: SecurityHubAwsKmsKeyDetails | None = None
    AwsLambdaFunction: SecurityHubAwsLambdaFunctionDetails | None = None
    AwsLambdaLayerVersion: SecurityHubAwsLambdaLayerVersionDetails | None = None
    AwsRdsDbInstance: SecurityHubAwsRdsDbInstanceDetails | None = None
    AwsSnsTopic: SecurityHubAwsSnsTopicDetails | None = None
    AwsSqsQueue: SecurityHubAwsSqsQueueDetails | None = None
    AwsWafWebAcl: SecurityHubAwsWafWebAclDetails | None = None
    AwsRdsDbSnapshot: SecurityHubAwsRdsDbSnapshotDetails | None = None
    AwsRdsDbClusterSnapshot: SecurityHubAwsRdsDbClusterSnapshotDetails | None = None
    AwsRdsDbCluster: SecurityHubAwsRdsDbClusterDetails | None = None
    AwsEcsCluster: SecurityHubAwsEcsClusterDetails | None = None
    AwsEcsContainer: SecurityHubAwsEcsContainerDetails | None = None
    AwsEcsTaskDefinition: SecurityHubAwsEcsTaskDefinitionDetails | None = None
    Container: SecurityHubContainerDetails | None = None
    Other: dict[StrictStr, StrictStr] | None = None
    AwsRdsEventSubscription: SecurityHubAwsRdsEventSubscriptionDetails | None = None
    AwsEcsService: SecurityHubAwsEcsServiceDetails | None = None
    AwsAutoScalingLaunchConfiguration: SecurityHubAwsAutoScalingLaunchConfigurationDetails | None = None
    AwsEc2VpnConnection: SecurityHubAwsEc2VpnConnectionDetails | None = None
    AwsEcrContainerImage: SecurityHubAwsEcrContainerImageDetails | None = None
    AwsOpenSearchServiceDomain: SecurityHubAwsOpenSearchServiceDomainDetails | None = None
    AwsEc2VpcEndpointService: SecurityHubAwsEc2VpcEndpointServiceDetails | None = None
    AwsXrayEncryptionConfig: SecurityHubAwsXrayEncryptionConfigDetails | None = None
    AwsWafRateBasedRule: SecurityHubAwsWafRateBasedRuleDetails | None = None
    AwsWafRegionalRateBasedRule: SecurityHubAwsWafRegionalRateBasedRuleDetails | None = None
    AwsEcrRepository: SecurityHubAwsEcrRepositoryDetails | None = None
    AwsEksCluster: SecurityHubAwsEksClusterDetails | None = None
    AwsNetworkFirewallFirewallPolicy: SecurityHubAwsNetworkFirewallFirewallPolicyDetails | None = None
    AwsNetworkFirewallFirewall: SecurityHubAwsNetworkFirewallFirewallDetails | None = None
    AwsNetworkFirewallRuleGroup: SecurityHubAwsNetworkFirewallRuleGroupDetails | None = None
    AwsRdsDbSecurityGroup: SecurityHubAwsRdsDbSecurityGroupDetails | None = None
    AwsKinesisStream: SecurityHubAwsKinesisStreamDetails | None = None
    AwsEc2TransitGateway: SecurityHubAwsEc2TransitGatewayDetails | None = None
    AwsEfsAccessPoint: SecurityHubAwsEfsAccessPointDetails | None = None
    AwsCloudFormationStack: SecurityHubAwsCloudFormationStackDetails | None = None
    AwsCloudWatchAlarm: SecurityHubAwsCloudWatchAlarmDetails | None = None
    AwsEc2VpcPeeringConnection: SecurityHubAwsEc2VpcPeeringConnectionDetails | None = None
    AwsWafRegionalRuleGroup: SecurityHubAwsWafRegionalRuleGroupDetails | None = None
    AwsWafRegionalRule: SecurityHubAwsWafRegionalRuleDetails | None = None
    AwsWafRegionalWebAcl: SecurityHubAwsWafRegionalWebAclDetails | None = None
    AwsWafRule: SecurityHubAwsWafRuleDetails | None = None
    AwsWafRuleGroup: SecurityHubAwsWafRuleGroupDetails | None = None
    AwsEcsTask: SecurityHubAwsEcsTaskDetails | None = None
    AwsBackupBackupVault: SecurityHubAwsBackupBackupVaultDetails | None = None
    AwsBackupBackupPlan: SecurityHubAwsBackupBackupPlanDetails | None = None
    AwsBackupRecoveryPoint: SecurityHubAwsBackupRecoveryPointDetails | None = None
    AwsEc2LaunchTemplate: SecurityHubAwsEc2LaunchTemplateDetails | None = None
    AwsSageMakerNotebookInstance: SecurityHubAwsSageMakerNotebookInstanceDetails | None = None
    AwsWafv2WebAcl: SecurityHubAwsWafv2WebAclDetails | None = None
    AwsWafv2RuleGroup: SecurityHubAwsWafv2RuleGroupDetails | None = None
    AwsEc2RouteTable: SecurityHubAwsEc2RouteTableDetails | None = None
    AwsAmazonMqBroker: SecurityHubAwsAmazonMqBrokerDetails | None = None
    AwsAppSyncGraphQlApi: SecurityHubAwsAppSyncGraphQlApiDetails | None = None
    AwsEventSchemasRegistry: SecurityHubAwsEventSchemasRegistryDetails | None = None
    AwsGuardDutyDetector: SecurityHubAwsGuardDutyDetectorDetails | None = None
    AwsStepFunctionStateMachine: SecurityHubAwsStepFunctionStateMachineDetails | None = None
    AwsAthenaWorkGroup: SecurityHubAwsAthenaWorkGroupDetails | None = None
    AwsEventsEventbus: SecurityHubAwsEventsEventbusDetails | None = None
    AwsDmsEndpoint: SecurityHubAwsDmsEndpointDetails | None = None
    AwsEventsEndpoint: SecurityHubAwsEventsEndpointDetails | None = None
    AwsDmsReplicationTask: SecurityHubAwsDmsReplicationTaskDetails | None = None
    AwsDmsReplicationInstance: SecurityHubAwsDmsReplicationInstanceDetails | None = None
    AwsRoute53HostedZone: SecurityHubAwsRoute53HostedZoneDetails | None = None
    AwsMskCluster: SecurityHubAwsMskClusterDetails | None = None
    AwsS3AccessPoint: SecurityHubAwsS3AccessPointDetails | None = None
    AwsEc2ClientVpnEndpoint: SecurityHubAwsEc2ClientVpnEndpointDetails | None = None
    CodeRepository: SecurityHubCodeRepositoryDetails | None = None
    AzureResource: SecurityHubAzureResourceDetails | None = None
    GcpResource: SecurityHubGcpResourceDetails | None = None
