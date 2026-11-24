from __future__ import annotations
from .cloud_watch_api_operation import CloudWatchAPIOperation
from .cloud_watch_api_operation_name import CloudWatchAPIOperationName
from .cloud_watch_api_operation_value import CloudWatchAPIOperationValue
from .cloud_watch_aws_services_map import CloudWatchAWSServicesMap
from .cloud_watch_service_name import CloudWatchServiceName


class CloudServiceAPIOpsMap:

    def __init__(self) -> None:

        self._api_ops_slug_map: dict[
            str,
            CloudWatchAPIOperation,
        ] = {
            service.name.lower().replace(
                '_',
                '-',
            ): service for service in CloudWatchAPIOperation
        }

        self._api_ops_map: dict[
            str,
            CloudWatchAPIOperation,
        ] = {
            service.name.lower().replace(
                '_',
                '',
            ): service for service in CloudWatchAPIOperation
        }

        self._api_ops_reverse_map: dict[
            str,
            str,
        ] = {
            operation.value: name for name, operation in self._api_ops_map.items()
        }
        self._api_ops_reverse_map.setdefault('ListDatasets', 'listdatasets')

        self._service_api_ops_map = {
            "DYNAMODB": [
                "accountprovisionedreadcapacityunits",
                "accountprovisionedwritecapacityunits"
            ],
            "ELASTICACHE": [
                "describecacheparametergroups",
                "nodesperregion",
                "describesnapshots",
                "describeserverlesscaches",
                "snapshotsperdaypercache",
                "cachesperregion",
                "describereplicationgroups",
                "parametergroup",
                "subnetspersubnetgroup",
                "describereservedcachenodes",
                "describeusers",
                "user",
                "usergroup",
                "usersperusergroup",
                "memcachednodespercluster",
                "describecachesubnetgroups"
            ],
            "CLOUDTRAIL": [
                "describetrails",
                "gettrailstatus",
                "getinsightselectors",
                "listchannels",
                "channel"
            ],
            "LOGS": [
                "describesubscriptionfilters",
                "describelogstreams",
                "describemetricfilters",
                "describeresourcepolicies",
                "createlogstream",
                "putlogevents",
                "describeloggroups",
                "describedestinations"
            ],
            "CLOUDSHELL": [
                "getenvironmentstatus",
                "deletesession"
            ],
            "EFS": [
                "describeaccesspoints"
            ],
            "EC2": [
                "describenetworkinsightsaccessscopes",
                "describetransitgatewayconnects",
                "describetransitgatewayroutetables",
                "describevpngateways",
                "getmanagedprefixlistentries",
                "describebyoipcidrs",
                "describeegressonlyinternetgateways",
                "describeaccountattributes",
                "describeflowlogs",
                "describeclientvpnendpoints",
                "describereservedinstancesmodifications",
                "describeipams",
                "describeipamresourcediscoveryassociations",
                "getsnapshotblockpublicaccessstate",
                "describefleets",
                "describetransitgateways",
                "describedhcpoptions",
                "describevpcendpointservices",
                "describeimages",
                "describecarriergateways",
                "describeinstanceconnectendpoints",
                "describespotinstancerequests",
                "describesnapshots",
                "describeverifiedaccesstrustproviders",
                "describevpcendpointconnectionnotifications",
                "describeinstancestatus",
                "describevpcendpointserviceconfigurations",
                "describevpcs",
                "describeipamscopes",
                "describeaddressesattribute",
                "describesecuritygroups",
                "describeipampools",
                "describetags",
                "describetrafficmirrortargets",
                "describetransitgatewayvpcattachments",
                "describescalabletargets",
                "describevpcblockpublicaccessexclusions",
                "describevpnconnections",
                "getinstancemetadatadefaults",
                "describeaddresses",
                "describeipamresourcediscoveries",
                "describehostreservations",
                "describevpcblockpublicaccessoptions",
                "getallowedimagessettings",
                "describeaccountlimits",
                "describesubnets",
                "describeverifiedaccessgroups",
                "describeautoscalinginstances",
                "describecapacityreservations",
                "describelaunchtemplateversions",
                "describereservedinstances",
                "describeautoscalinggroups",
                "describesecuritygrouprules",
                "describenetworkinsightsanalyses",
                "describespotfleetrequests",
                "describevpcendpoints",
                "describeregions",
                "getimageblockpublicaccessstate",
                "getebsencryptionbydefault",
                "describefpgaimages",
                "describenetworkinsightspaths",
                "describescalingpolicies",
                "describecoippools",
                "describetransitgatewayroutetableannouncements",
                "describecapacityreservationfleets",
                "describeinternetgateways",
                "describetransitgatewayconnectpeers",
                "describeinstancetypes",
                "describelaunchconfigurations",
                "describenetworkinterfaces",
                "describelocalgatewayroutetables",
                "describenatgateways",
                "describetransitgatewayattachments",
                "describeplacementgroups",
                "describeinstances",
                "describenetworkinsightsaccessscopeanalyses"
            ],
            "RDS": [
                "describedbsnapshots",
                "describereserveddbinstances",
                "describedbinstances",
                "describeoptiongroups",
                "describedbclusters",
                "describedbsecuritygroups",
                "describeaccountattributes",
                "describedbclusterparametergroups",
                "describedbclustersnapshots",
                "describedbclusterendpoints",
                "describedbinstanceautomatedbackups",
                "describebluegreendeployments",
                "describeeventsubscriptions",
                "describeglobalclusters",
                "describependingmaintenanceactions",
                "describedbsubnetgroups"
            ],
            "CLOUDFORMATION": [
                "gettemplatesummary",
                "listtypes",
                "getstackpolicy",
                "describeorganizationsaccess",
                "listchangesets",
                "liststacks",
                "liststackresources",
                "gettemplate",
                "describeaccountlimits",
                "stackinstanceoperations",
                "liststacksets",
                "describestacks"
            ],
            "MEMORYDB": [
                "describeacls",
                "describesnapshots",
                "describeusers",
                "describesubnetgroups",
                "describeclusters",
                "describeparametergroups"
            ],
            "SES": [
                "getaccount",
                "listreceiptfilters",
                "listemailtemplates",
                "listreceiptrulesets",
                "listemailidentities",
                "describeactivereceiptruleset",
                "listconfigurationsets",
                "listcontactlists"
            ],
            "CLOUDWATCH": [
                "getmetricdata",
                "getmetricstatistics",
                "describeinsightrules",
                "listapplications",
                "listtagsforresource",
                "listmetrics",
                "describealarms"
            ],
            "ELASTIC": [
                "describeenvironments",
                "describesslpolicies",
                "describetargetgroups",
                "describeapplications",
                "describeapplicationversions"
            ],
            "BACKUP": [
                "listtags",
                "listrecoverypointsbybackupvault",
                "listbackupplans",
                "describebackupvault",
                "getbackupvaultaccesspolicy"
            ],
            "CLOUDHSM": [
                "describeclusters"
            ],
            "REDSHIFT": [
                "describeclustersnapshots",
                "describeendpointaccess",
                "describesnapshotschedules",
                "describeendpointauthorization",
                "describeclustersecuritygroups",
                "describeclusters",
                "describeclustersubnetgroups",
                "describeeventsubscriptions",
                "describeusagelimits",
                "describereservednodes"
            ],
            "AWS": [
                "listdatastores",
                "describecompliancebyresource",
                "getcompliancedetailsbyconfigrule",
                "listdeploymentstrategies",
                "describeconfigurationrecorders",
                "getresourcepolicy",
                "getdiscoveredresourcecounts",
                "getdeploymentstrategy",
                "listdomains",
                "describeremediationconfigurations",
                "selectresourceconfig",
                "describeconfigruleevaluationstatus",
                "getdatabases",
                "describependingaggregationrequests",
                "listdiscoveredresources",
                "listrepositories",
                "putevaluations",
                "describeconfigrules",
                "listconfigurationrecorders",
                "describeconfigurationrecorderstatus",
                "describecompliancebyconfigrule",
                "listnotificationhubs",
                "listapplications",
                "listtagsforresource",
                "listextensionassociations"
            ],
            "BATCH": [
                "describecomputeenvironments",
                "describejobdefinitions",
                "listschedulingpolicies",
                "describejobqueues"
            ],
            "KMS": [
                "describekey",
                "listkeys",
                "listresourcetags",
                "keysperaccount",
                "describecustomkeystores",
                "listkeyrotations",
                "getkeypolicy",
                "listgrants",
                "listaliases"
            ],
            "DIRECTORY": [
                "describedirectories"
            ],
            "SSM": [
                "getparameter",
                "describeparameters",
                "listassociations",
                "describemaintenancewindows",
                "listdocuments",
                "describedocument",
                "describeinstanceinformation",
                "describedocumentpermission",
                "getservicesetting",
                "listresourcedatasync"
            ],
            "EVENTBRIDGE": [
                "describeeventbus",
                "listrules",
                "listtargetsbyrule",
                "listapidestinations",
                "listeventbuses",
                "listarchives",
                "listtagsforresource",
                "listendpoints"
            ],
            "DATABASE": [
                "describereplicationsubnetgroups",
                "describereplicationinstances",
                "describeeventsubscriptions"
            ],
            "GAMELIFT": [
                "describematchmakingconfigurations",
                "describegamesessionqueues",
                "describefleetattributes",
                "listgameservergroups",
                "listlocations",
                "listaliases"
            ],
            "APPSTREAM": [
                "describeimagebuilders",
                "describestacks",
                "describefleets"
            ],
            "KINESIS": [
                "listsignalingchannels",
                "liststreams",
                "listapplications",
                "describelimits"
            ],
            "ECR": [
                "describeregistry",
                "getregistryscanningconfiguration",
                "describepullthroughcacherules",
                "describerepositories",
                "getregistrypolicy",
                "getaccountsetting"
            ],
            "SECRETS": [
                "getsecretvalue",
                "listsecrets",
                "describesecret"
            ],
            "SECURITY": [
                "listmembers",
                "describestandardscontrols",
                "getenabledstandards",
                "getfindings",
                "getadministratoraccount",
                "listtagsforresource",
                "listinvitations",
                "listenabledproductsforimport"
            ],
            "WORKSPACES": [
                "describeworkspaces"
            ],
            "COMPUTEOPTIMIZER": [
                "exportlambdafunctionrecommendations",
                "exportec2instancerecommendations",
                "getrecommendationsummaries",
                "exportlicenserecommendations",
                "getenrollmentstatus",
                "exportecsservicerecommendations",
                "exportautoscalinggrouprecommendations",
                "exportrdsdatabaserecommendations",
                "getrdsdatabaserecommendations",
                "exportebsvolumerecommendations"
            ],
            "RESOURCE": [
                "getresources",
                "getresourceshares",
                "getaccountsettings",
                "listgroups"
            ],
            "LAMBDA": [
                "listversionsbyfunction20150331",
                "listlayers20181031",
                "getfunctionurlconfig",
                "getaccountsettings20160819",
                "listcodesigningconfigs",
                "listfunctions20150331",
                "getpolicy20150331",
                "listfunctionurlconfigs",
                "getfunction20150331v2"
            ],
            "AUDIT": [
                "getaccountstatus"
            ],
            "API": [
                "getdomainnames",
                "getvpclinks",
                "getapis"
            ],
            "PINPOINT": [
                "getapps",
                "listtemplates"
            ],
            "EMR": [
                "listsecurityconfigurations",
                "getblockpublicaccessconfiguration",
                "listclusters",
                "listvirtualclusters",
                "listapplications"
            ],
            "AMAZON": [
                "listvaults",
                "listsecurityconfigurations",
                "listdatasets",
                "getblockpublicaccessconfiguration",
                "listorganizations",
                "listclusters",
                "listbots"
            ],
            "LIGHTSAIL": [
                "getcertificates",
                "getstaticips",
                "getblueprints",
                "getbuckets",
                "getcontainerservices",
                "getrelationaldatabases"
            ],
            "S3": [
                "getbucketcors",
                "listmultiregionaccesspoints",
                "getbucketownershipcontrols",
                "getbucketlocation",
                "getbucketacl",
                "getbucketversioning",
                "getbucketobjectlockconfiguration",
                "getbucketlogging",
                "getbucketwebsite",
                "getbucketencryption",
                "getbucketreplication",
                "getbucketrequestpayment",
                "getbucketnotification",
                "getbucketlifecycle",
                "listaccesspoints",
                "liststoragelensgroups",
                "listbuckets",
                "getbucketintelligenttieringconfiguration",
                "getbucketmetricsconfiguration"
            ],
            "ATHENA": [
                "getdatacatalog",
                "listpreparedstatements",
                "getworkgroup",
                "listtagsforresource",
                "listworkgroups",
                "listdatacatalogs"
            ],
            "GUARDDUTY": [
                "listmembers",
                "listdetectors",
                "listpublishingdestinations",
                "getdetector",
                "getinvitationscount",
                "getmalwarescansettings",
                "getmasteraccount",
                "listfilters",
                "listthreatintelsets"
            ],
            "FRAUD": [
                "getdetectors",
                "getentitytypes",
                "getexternalmodels",
                "getvariables",
                "getoutcomes",
                "geteventtypes"
            ],
            "X_RAY": [
                "getencryptionconfig"
            ],
            "DATA": [
                "listdatasets",
                "getlifecyclepolicies"
            ],
            "MACIE": [
                "getmaciesession"
            ],
            "ROUTE": [
                "listresolverquerylogconfigs",
                "listfirewalldomainlists",
                "listresolverendpoints",
                "getresolverrule"
            ],
            "SERVICE": [
                "getservicequota",
                "listapplications",
                "listattributegroups"
            ],
            "SNS": [
                "gettopicattributes",
                "listsubscriptions",
                "numberofmessagespublishedperaccount",
                "listtagsforresource",
                "listsubscriptionsbytopic"
            ],
            "BEDROCK": [
                "listagents"
            ],
            "IOT": [
                "listinputs",
                "listrolealiases",
                "listcertificates",
                "listcustommetrics",
                "listalarmmodels",
                "listserviceprofiles",
                "listworkspaces",
                "listfleetmetrics",
                "listdetectormodels",
                "listthings",
                "listpolicies",
                "listassetmodels",
                "listcacertificates",
                "listdimensions",
                "listfuotatasks",
                "listmitigationactions",
                "listsecurityprofiles",
                "listtopicruledestinations",
                "listgateways",
                "listscheduledaudits",
                "listportals",
                "listmulticastgroups"
            ],
            "ACCESS": [
                "listanalyzers",
                "listarchiverules"
            ],
            "APPINTEGRATIONS": [
                "listapplications",
                "listeventintegrations"
            ],
            "MEDIACONNECT": [
                "listgateways",
                "listflows",
                "listbridges"
            ],
            "TRANSCRIBE": [
                "listcallanalyticsjobs",
                "listvocabularies",
                "listmedicaltranscriptionjobs",
                "listmedicalvocabularies",
                "listmedicalscribejobs",
                "listlanguagemodels"
            ],
            "PRIVATE": [
                "listcertificateauthorities"
            ],
            "CERTIFICATE": [
                "listcertificates"
            ],
            "TRANSFER": [
                "listservers",
                "listprofiles",
                "listcertificates",
                "listworkflows"
            ],
            "EKS": [
                "listclusters"
            ],
            "SAGEMAKER": [
                "listfeaturegroups",
                "listworkteams",
                "listpipelines",
                "listnotebookinstancelifecycleconfigs",
                "listcoderepositories",
                "listendpointconfigs",
                "listdomains",
                "listendpoints",
                "listimages",
                "listinferenceexperiments"
            ],
            "CLEAN": [
                "listcollaborations"
            ],
            "GREENGRASS": [
                "listfunctiondefinitions",
                "listcomponents",
                "listresourcedefinitions",
                "listdevicedefinitions",
                "listloggerdefinitions",
                "listgroups",
                "listconnectordefinitions"
            ],
            "IMAGE": [
                "listinfrastructureconfigurations",
                "listcomponents",
                "listimagerecipes",
                "listdistributionconfigurations",
                "listimages",
                "listcontainerrecipes"
            ],
            "GROUND": [
                "listmissionprofiles",
                "listconfigs"
            ],
            "MEDIASTORE": [
                "listcontainers"
            ],
            "DATABREW": [
                "listdatasets",
                "listrulesets",
                "listprojects",
                "listschedules",
                "listrecipes"
            ],
            "COMPREHEND": [
                "listeventsdetectionjobs",
                "listpiientitiesdetectionjobs",
                "listdominantlanguagedetectionjobs",
                "listentityrecognizers",
                "listsentimentdetectionjobs",
                "listdocumentclassifiers",
                "listflywheels",
                "listkeyphrasesdetectionjobs",
                "listtopicsdetectionjobs",
                "listentitiesdetectionjobs"
            ],
            "CUSTOMER": [
                "listdomains"
            ],
            "NETWORK": [
                "listfirewallpolicies",
                "listfirewalls"
            ],
            "APPFLOW": [
                "listflows"
            ],
            "NEPTUNEGRAPH": [
                "listgraphsnapshots",
                "listgraphs"
            ],
            "DETECTIVE": [
                "listgraphs"
            ],
            "CONNECT": [
                "listinstances",
                "listphonenumbersv2"
            ],
            "QLDB": [
                "listledgers"
            ],
            "IVSCHAT": [
                "listloggingconfigurations"
            ],
            "LOCATION": [
                "listtrackers",
                "listmaps"
            ],
            "CODESTAR": [
                "listnotificationrules"
            ],
            "TRANSLATE": [
                "listterminologies",
                "listparalleldata",
                "listtexttranslationjobs"
            ],
            "CODEPIPELINE": [
                "listpipelines"
            ],
            "MEDIATAILOR": [
                "listplaybackconfigurations"
            ],
            "IVS": [
                "listrecordingconfigurations",
                "listplaybackkeypairs"
            ],
            "MEDIACONVERT": [
                "listpresets"
            ],
            "LOOKOUT": [
                "listprojects"
            ],
            "CODEBUILD": [
                "listreportgroups",
                "listprojects"
            ],
            "CODECOMMIT": [
                "listrepositories"
            ],
            "ROBOMAKER": [
                "listsimulationapplications",
                "listrobotapplications"
            ],
            "SCHEDULER": [
                "listschedules",
                "listschedulegroups"
            ],
            "CLOUD": [
                "listservices"
            ],
            "OUTPOSTS": [
                "listsites"
            ],
            "ECS": [
                "listtagsforresource"
            ],
            "DATASYNC": [
                "listtasks"
            ],
            "COGNITO": [
                "userpoolread",
                "listuserpools"
            ],
            "GRAFANA": [
                "listworkspaces"
            ]
        }

        self._services = CloudWatchAWSServicesMap()

    def get(self, operation_name: CloudWatchAPIOperationName):
        return self._api_ops_map[operation_name]
    
    def get_by_slug(self, operation_slug: str):
        return self._api_ops_slug_map[operation_slug]
    
    def get_api_operation_slug(self, operation: CloudWatchAPIOperationValue):
        return self._api_ops_reverse_map[operation]
    
    def get_service_operations(self, service_name: CloudWatchServiceName) -> list[str]:
        service = self._services.get(service_name)
        for key in (
            service.name,
            service.name.replace('_', ''),
            service.name.split('_')[0],
        ):
            if key in self._service_api_ops_map:
                return self._service_api_ops_map[key]
        return []
