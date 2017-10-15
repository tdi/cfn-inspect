# cfn-inspect: pretty print and inspect CloudFormation templates

Simple pretty printer for CloudFormation templates, in future it will also provide some validation and deep inspection. 

Support json templates only for now. 


# Installation

```$ pip install cfn-inspect```

# Usage 

```
$ cfn-inspect rds.json --verbose

cfn-inspect v0.1
Inspecting template: templates/rds.json
Description: RDS-MySQL
Parameters
  AllocatedStorage (Number)
  DbMasterPassword (String)
  DbName (String)
  ExistingDbSnapshot (String)
  NetworkStack (String)
  Production (String)
Resources
  DbMysql (AWS::RDS::DBInstance)
  SecurityGroupClientMysql (AWS::EC2::SecurityGroup)
  SecurityGroupDbMysql (AWS::EC2::SecurityGroup)
Outputs
  ClientSG
  DbHost
    Exported as {'Fn::Sub': '${AWS::StackName}-DbHost'}
  DbMasterUser
    Exported as {'Fn::Sub': '${AWS::StackName}-DbMasterUser'}
  DbMysql
    Exported as {'Fn::Sub': '${AWS::StackName}-DbMysql'}
  DbName
    Exported as {'Fn::Sub': '${AWS::StackName}-DbName'}
  DbPort
    Exported as {'Fn::Sub': '${AWS::StackName}-DbPort'}
```

# Author
Dariusz Dwornikowski
