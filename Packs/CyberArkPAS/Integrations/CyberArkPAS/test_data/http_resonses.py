ADD_USER_RAW_RESPONSE = {"authenticationMethod": ["AuthTypePass"],
                             "businessAddress": {"workCity": "", "workCountry": "", "workState": "", "workStreet": "",
                                                 "workZip": ""}, "changePassOnNextLogon": True, "componentUser": False,
                             "description": "new user for test", "distinguishedName": "", "enableUser": True,
                             "expiryDate": -62135578800, "groupsMembership": [], "id": 123,
                             "internet": {"businessEmail": "usertest@test.com", "homeEmail": "", "homePage": "",
                                          "otherEmail": ""}, "lastSuccessfulLoginDate": 1594756313, "location": "\\",
                             "passwordNeverExpires": False,
                             "personalDetails": {"city": "", "country": "", "department": "", "firstName": "user",
                                                 "lastName": "test", "middleName": "", "organization": "",
                                                 "profession": "testing integrations", "state": "", "street": "",
                                                 "title": "", "zip": ""},
                             "phones": {"businessNumber": "", "cellularNumber": "", "faxNumber": "", "homeNumber": "",
                                        "pagerNumber": ""}, "source": "CyberArkPAS", "suspended": False,
                             "unAuthorizedInterfaces": [], "userType": "EPVUser", "username": "TestUser",
                             "vaultAuthorization": []}

UPDATE_USER_RAW_RESPONSE = {"authenticationMethod": ["AuthTypePass"],
                            "businessAddress": {"workCity": "", "workCountry": "", "workState": "", "workStreet": "",
                                                "workZip": ""},
                            "changePassOnNextLogon": True, "componentUser": False, "description": "updated description",
                            "distinguishedName": "", "enableUser": True, "expiryDate": -62135578800,
                            "groupsMembership": [], "id": 123,
                            "internet": {"businessEmail": "update@test.com", "homeEmail": "", "homePage": "",
                                         "otherEmail": ""},
                            "lastSuccessfulLoginDate": 1594756313, "location": "\\", "passwordNeverExpires": False,
                            "personalDetails": {"city": "", "country": "", "department": "", "firstName": "test1",
                                                "lastName": "updated-name",
                                                "middleName": "", "organization": "", "profession": "test1",
                                                "state": "", "street": "",
                                                "title": "", "zip": ""},
                            "phones": {"businessNumber": "", "cellularNumber": "", "faxNumber": "", "homeNumber": "",
                                       "pagerNumber": ""},
                            "source": "CyberArkPAS", "suspended": False, "unAuthorizedInterfaces": [],
                            "userType": "EPVUser",
                            "username": "TestUser1", "vaultAuthorization": []}

GET_USERS_RAW_RESPONSE = {"Total": 2, "Users": [{"componentUser": False, "id": 2, "location": "\\",
                                                  "personalDetails": {"firstName": "", "lastName": "",
                                                                      "middleName": ""}, "source": "CyberArkPAS",
                                                  "userType": "Built-InAdmins", "username": "Administrator",
                                                  "vaultAuthorization": ["AddUpdateUsers", "AddSafes",
                                                                         "AddNetworkAreas",
                                                                         "ManageDirectoryMapping",
                                                                         "ManageServerFileCategories", "AuditUsers",
                                                                         "BackupAllSafes", "RestoreAllSafes",
                                                                         "ResetUsersPasswords", "ActivateUsers"]},
                                                 {"componentUser": False, "id": 3, "location": "\\",
                                                  "personalDetails": {"firstName": "", "lastName": "",
                                                                      "middleName": ""}, "source": "CyberArkPAS",
                                                  "userType": "Built-InAdmins", "username": "Auditor",
                                                  "vaultAuthorization": ["AuditUsers"]}]}

ADD_SAFE_RAW_RESPONSE = {"AutoPurgeEnabled": False, "Description": "safe for tests", "Location": "\\",
                         "ManagingCPM": "",
                         "NumberOfDaysRetention": 100, "NumberOfVersionsRetention": None, "OLACEnabled": True,
                         "SafeName": "TestSafe"}

UPDATE_SAFE_RAW_RESPONSE = {"AutoPurgeEnabled": False, "Description": "UpdatedSafe", "Location": "\\",
                            "ManagingCPM": "", "NumberOfDaysRetention": 150, "NumberOfVersionsRetention": None,
                            "OLACEnabled": True, "SafeName": "UpdatedName"}

GET_SAFE_BY_NAME_RAW_RESPONSE = {"AutoPurgeEnabled": False, "Description": "safe for tests", "Location": "\\",
                            "ManagingCPM": "", "NumberOfDaysRetention": 100, "NumberOfVersionsRetention": None,
                            "OLACEnabled": True, "SafeName": "TestSafe"}

GET_LIST_SAFES_RAW_RESPONSE = {
    "Safes": [{"Description": "", "Location": "\\", "SafeName": "VaultInternal", "SafeUrlId": "VaultInternal"},
              {"Description": "", "Location": "\\", "SafeName": "Notification Engine",
               "SafeUrlId": "Notification%20Engine"}]}


ADD_SAFE_MEMBER_RAW_RESPONSE = {"member": {"MemberName": "TestUser", "MembershipExpirationDate": "",
                                      "Permissions": [{"Key": "UseAccounts", "Value": False},
                                                      {"Key": "RetrieveAccounts", "Value": False},
                                                      {"Key": "ListAccounts", "Value": False},
                                                      {"Key": "AddAccounts", "Value": False},
                                                      {"Key": "UpdateAccountContent", "Value": False},
                                                      {"Key": "UpdateAccountProperties", "Value": False},
                                                      {"Key": "InitiateCPMAccountManagementOperations",
                                                       "Value": False},
                                                      {"Key": "SpecifyNextAccountContent", "Value": False},
                                                      {"Key": "RenameAccounts", "Value": False},
                                                      {"Key": "DeleteAccounts", "Value": False},
                                                      {"Key": "UnlockAccounts", "Value": False},
                                                      {"Key": "ManageSafe", "Value": False},
                                                      {"Key": "ManageSafeMembers", "Value": False},
                                                      {"Key": "BackupSafe", "Value": False},
                                                      {"Key": "ViewAuditLog", "Value": False},
                                                      {"Key": "ViewSafeMembers", "Value": False},
                                                      {"Key": "AccessWithoutConfirmation", "Value": False},
                                                      {"Key": "CreateFolders", "Value": False},
                                                      {"Key": "DeleteFolders", "Value": False},
                                                      {"Key": "MoveAccountsAndFolders", "Value": False},
                                                      {"Key": "RequestsAuthorizationLevel", "Value": 0}],
                                      "SearchIn": "vault"}}

UPDATE_SAFE_MEMBER_RAW_RESPONSE = {"member": {"MemberName": "TestUser", "MembershipExpirationDate": "",
                                         "Permissions": [{"Key": "UseAccounts", "Value": True},
                                                         {"Key": "RetrieveAccounts", "Value": False},
                                                         {"Key": "ListAccounts", "Value": False},
                                                         {"Key": "AddAccounts", "Value": False},
                                                         {"Key": "UpdateAccountContent", "Value": False},
                                                         {"Key": "UpdateAccountProperties", "Value": False},
                                                         {"Key": "InitiateCPMAccountManagementOperations",
                                                          "Value": False},
                                                         {"Key": "SpecifyNextAccountContent", "Value": False},
                                                         {"Key": "RenameAccounts", "Value": False},
                                                         {"Key": "DeleteAccounts", "Value": False},
                                                         {"Key": "UnlockAccounts", "Value": False},
                                                         {"Key": "ManageSafe", "Value": False},
                                                         {"Key": "ManageSafeMembers", "Value": False},
                                                         {"Key": "BackupSafe", "Value": False},
                                                         {"Key": "ViewAuditLog", "Value": False},
                                                         {"Key": "ViewSafeMembers", "Value": False},
                                                         {"Key": "AccessWithoutConfirmation", "Value": False},
                                                         {"Key": "CreateFolders", "Value": False},
                                                         {"Key": "DeleteFolders", "Value": False},
                                                         {"Key": "MoveAccountsAndFolders", "Value": False},
                                                         {"Key": "RequestsAuthorizationLevel", "Value": 0}],
                                         "SearchIn": "vault"}}

LIST_SAFE_MEMBER_RAW_RESPONSE = {"SafeMembers": [
    {"IsExpiredMembershipEnable": False, "IsPredefinedUser": True, "MemberName": "Administrator",
     "MemberType": "User", "MembershipExpirationDate": None,
     "Permissions": {"AccessWithoutConfirmation": True, "AddAccounts": True, "BackupSafe": True,
                     "CreateFolders": True, "DeleteAccounts": True, "DeleteFolders": True,
                     "InitiateCPMAccountManagementOperations": True, "ListAccounts": True, "ManageSafe": True,
                     "ManageSafeMembers": True, "MoveAccountsAndFolders": True, "RenameAccounts": True,
                     "RequestsAuthorizationLevel1": True, "RequestsAuthorizationLevel2": False,
                     "RetrieveAccounts": True, "SpecifyNextAccountContent": True, "UnlockAccounts": True,
                     "UpdateAccountContent": True, "UpdateAccountProperties": True, "UseAccounts": True,
                     "ViewAuditLog": True, "ViewSafeMembers": True}},
    {"IsExpiredMembershipEnable": False, "IsPredefinedUser": True, "MemberName": "Master", "MemberType": "User",
     "MembershipExpirationDate": None,
     "Permissions": {"AccessWithoutConfirmation": True, "AddAccounts": True, "BackupSafe": True,
                     "CreateFolders": True, "DeleteAccounts": True, "DeleteFolders": True,
                     "InitiateCPMAccountManagementOperations": True, "ListAccounts": True, "ManageSafe": True,
                     "ManageSafeMembers": True, "MoveAccountsAndFolders": True, "RenameAccounts": True,
                     "RequestsAuthorizationLevel1": False, "RequestsAuthorizationLevel2": False,
                     "RetrieveAccounts": True, "SpecifyNextAccountContent": True, "UnlockAccounts": True,
                     "UpdateAccountContent": True, "UpdateAccountProperties": True, "UseAccounts": True,
                     "ViewAuditLog": True, "ViewSafeMembers": True}}]}

ADD_ACCOUNT_RAW_RESPONSE = {"address": "/", "categoryModificationTime": 1594835018, "createdTime": 1594838456,
                            "id": "77_4",
                            "name": "TestAccount1", "platformId": "WinServerLocal", "safeName": "TestSafe",
                            "secretManagement": {"automaticManagementEnabled": True,
                                                 "lastModifiedTime": 1594824056}, "secretType": "password",
                            "userName": "TestUser"}

UPDATE_ACCOUNT_RAW_RESPONSE = {"address": "/", "categoryModificationTime": 1594835018, "createdTime": 1594838456,
                               "id": "77_4", "name": "NewName", "platformId": "WinServerLocal",
                               "safeName": "TestSafe", "secretManagement": {"automaticManagementEnabled": True,
                                                                            "lastModifiedTime": 1594824056},
                               "secretType": "password", "userName": "TestUser"}

GET_LIST_ACCOUNT_RAW_RESPONSE = {"count": 2, "nextLink": "api/Accounts?offset=2\u0026limit=2", "value": [
    {"address": "string", "categoryModificationTime": 1594569595, "createdTime": 1594573679, "id": "2_6",
     "name": "account1", "platformAccountProperties": {}, "platformId": "Oracle", "safeName": "VaultInternal",
     "secretManagement": {"automaticManagementEnabled": True, "lastModifiedTime": 1594559279},
     "secretType": "password", "userName": "string"},
    {"address": "10.0.0.5", "categoryModificationTime": 1583345933, "createdTime": 1573127750, "id": "2_3",
     "name": "cybr.com.pass", "platformAccountProperties": {}, "platformId": "WinDomain",
     "safeName": "VaultInternal",
     "secretManagement": {"automaticManagementEnabled": False, "lastModifiedTime": 1573109750,
                          "manualManagementReason": "NoReason"}, "secretType": "password",
     "userName": "vaultbind@cybr.com"}]}

GET_LIST_ACCOUNT_ACTIVITIES_RAW_RESPONSE = {"Activities": [
    {"Action": "Rename File", "ActionID": 124, "Alert": False, "ClientID": "PVWA", "Date": 1594838533,
     "MoreInfo": "NewName", "Reason": "", "User": "Administrator"},
    {"Action": "Store password", "ActionID": 294, "Alert": False, "ClientID": "PVWA", "Date": 1594838456,
     "MoreInfo": "", "Reason": "", "User": "Administrator"}]}

GET_SECURITY_EVENTS = [
    {
        "id": "5f0ea000e4b0ba4baf5d1910",
        "type": "VaultViaIrregularIp",
        "score": 27.656250000000004,
        "createTime": 1594793984000,
        "lastUpdateTime": 1594793984000,
        "audits": [
            {
                "id": "5f0ea000e4b0ba4baf5d190e",
                "type": "VAULT_LOGON",
                "sensorType": "VAULT",
                "action": "Logon",
                "createTime": 1594793984000,
                "vaultUser": "Administrator",
                "source": {
                    "mOriginalAddress": "82.166.99.178"
                },
                "cloudData": {}
            }
        ],
        "additionalData": {
            "station": "82.166.99.178",
            "reason": "ip",
            "vault_user": "administrator"
        },
        "mStatus": "OPEN"
    },
    {
        "id": "5f0c5b5de4b0ba4baf5c66db",
        "type": "VaultViaIrregularIp",
        "score": 29.414062500000004,
        "createTime": 1594645338000,
        "lastUpdateTime": 1594645338000,
        "audits": [
            {
                "id": "5f0c5b5de4b0ba4baf5c653e",
                "type": "VAULT_LOGON",
                "sensorType": "VAULT",
                "action": "Logon",
                "createTime": 1594645338000,
                "vaultUser": "Administrator",
                "source": {
                    "mOriginalAddress": "46.116.46.136",
                    "mResolvedAddress": {
                        "mOriginalAddress": "46.116.46.136",
                        "mAddress": "46.116.46.136",
                        "mHostName": "46-116-46-136",
                        "mFqdn": "46-116-46-136.bb.netvision.net.il"
                    }
                },
                "cloudData": {}
            }
        ],
        "additionalData": {
            "station": "46.116.46.136",
            "reason": "ip",
            "vault_user": "administrator"
        },
        "mStatus": "OPEN"
    },
    {
        "id": "5f0b4e53e4b0ba4baf5c43ed",
        "type": "VaultViaIrregularIp",
        "score": 29.414062500000004,
        "createTime": 1594576467000,
        "lastUpdateTime": 1594576467000,
        "audits": [
            {
                "id": "5f0b4e53e4b0ba4baf5c43eb",
                "type": "VAULT_LOGON",
                "sensorType": "VAULT",
                "action": "Logon",
                "createTime": 1594576467000,
                "vaultUser": "Administrator",
                "source": {
                    "mOriginalAddress": "46.116.46.136",
                    "mResolvedAddress": {
                        "mOriginalAddress": "46.116.46.136",
                        "mAddress": "46.116.46.136",
                        "mHostName": "46-116-46-136",
                        "mFqdn": "46-116-46-136.bb.netvision.net.il"
                    }
                },
                "cloudData": {}
            }
        ],
        "additionalData": {
            "station": "46.116.46.136",
            "reason": "ip",
            "vault_user": "administrator"
        },
        "mStatus": "OPEN"
    },
    {
        "id": "5f0b4320e4b0ba4baf5c2b05",
        "type": "VaultViaIrregularIp",
        "score": 29.414062500000004,
        "createTime": 1594573600000,
        "lastUpdateTime": 1594573600000,
        "audits": [
            {
                "id": "5f0b4320e4b0ba4baf5c2b03",
                "type": "VAULT_LOGON",
                "sensorType": "VAULT",
                "action": "Logon",
                "createTime": 1594573600000,
                "vaultUser": "Administrator",
                "source": {
                    "mOriginalAddress": "46.116.46.136",
                    "mResolvedAddress": {
                        "mOriginalAddress": "46.116.46.136",
                        "mAddress": "46.116.46.136",
                        "mHostName": "46-116-46-136",
                        "mFqdn": "46-116-46-136.bb.netvision.net.il"
                    }
                },
                "cloudData": {}
            }
        ],
        "additionalData": {
            "station": "46.116.46.136",
            "reason": "ip",
            "vault_user": "administrator"
        },
        "mStatus": "OPEN"
    },
    {
        "id": "5f0b3064e4b0ba4baf5c1113",
        "type": "VaultViaIrregularIp",
        "score": 29.414062500000004,
        "createTime": 1594568804000,
        "lastUpdateTime": 1594568804000,
        "audits": [
            {
                "id": "5f0b3064e4b0ba4baf5c1111",
                "type": "VAULT_LOGON",
                "sensorType": "VAULT",
                "action": "Logon",
                "createTime": 1594568804000,
                "vaultUser": "Administrator",
                "source": {
                    "mOriginalAddress": "46.116.46.136",
                    "mResolvedAddress": {
                        "mOriginalAddress": "46.116.46.136",
                        "mAddress": "46.116.46.136",
                        "mHostName": "46-116-46-136",
                        "mFqdn": "46-116-46-136.bb.netvision.net.il"
                    }
                },
                "cloudData": {}
            }
        ],
        "additionalData": {
            "station": "46.116.46.136",
            "reason": "ip",
            "vault_user": "administrator"
        },
        "mStatus": "OPEN"
    }]
