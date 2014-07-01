import datetime
import logging
import nabcommerce
print("See source for links to documentation")

print "\n","########   Preparing the application to Transact ########","\n"
# https://my.ipcommerce.com/Docs/1.17.16/CWS_REST_Developer_Guide/RESTImplementation/PreparingTheAppToTransact/index.aspx

print "\n","********   Step 1 - Sign On Authentication   **********","\n"
# https://my.ipcommerce.com/Docs/1.17.16/CWS_REST_Developer_Guide/RESTImplementation/PreparingTheAppToTransact/SignOnAuthentication/index.aspx

identity_token = "PHNhbWw6QXNzZXJ0aW9uIE1ham9yVmVyc2lvbj0iMSIgTWlub3JWZXJzaW9uPSIxIiBBc3NlcnRpb25JRD0iX2YwYzdlOWQyLWIxOGMtNGE3NS1hMTI1LWIyOTNjMjBkNGZiMyIgSXNzdWVyPSJJcGNBdXRoZW50aWNhdGlvbiIgSXNzdWVJbnN0YW50PSIyMDE0LTA0LTAyVDE5OjIzOjM1LjExOFoiIHhtbG5zOnNhbWw9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjEuMDphc3NlcnRpb24iPjxzYW1sOkNvbmRpdGlvbnMgTm90QmVmb3JlPSIyMDE0LTA0LTAyVDE5OjIzOjM1LjExOFoiIE5vdE9uT3JBZnRlcj0iMjAxNy0wNC0wMlQxOToyMzozNS4xMThaIj48L3NhbWw6Q29uZGl0aW9ucz48c2FtbDpBZHZpY2U+PC9zYW1sOkFkdmljZT48c2FtbDpBdHRyaWJ1dGVTdGF0ZW1lbnQ+PHNhbWw6U3ViamVjdD48c2FtbDpOYW1lSWRlbnRpZmllcj5BRkY0RjYyRTNEQjAwMDAxPC9zYW1sOk5hbWVJZGVudGlmaWVyPjwvc2FtbDpTdWJqZWN0PjxzYW1sOkF0dHJpYnV0ZSBBdHRyaWJ1dGVOYW1lPSJTQUsiIEF0dHJpYnV0ZU5hbWVzcGFjZT0iaHR0cDovL3NjaGVtYXMuaXBjb21tZXJjZS5jb20vSWRlbnRpdHkiPjxzYW1sOkF0dHJpYnV0ZVZhbHVlPkFGRjRGNjJFM0RCMDAwMDE8L3NhbWw6QXR0cmlidXRlVmFsdWU+PC9zYW1sOkF0dHJpYnV0ZT48c2FtbDpBdHRyaWJ1dGUgQXR0cmlidXRlTmFtZT0iU2VyaWFsIiBBdHRyaWJ1dGVOYW1lc3BhY2U9Imh0dHA6Ly9zY2hlbWFzLmlwY29tbWVyY2UuY29tL0lkZW50aXR5Ij48c2FtbDpBdHRyaWJ1dGVWYWx1ZT5hZDQwMWQ1Yy1hNzZmLTRlYWItYmU5ZC1mNjU2NjlmOWE0ZTg8L3NhbWw6QXR0cmlidXRlVmFsdWU+PC9zYW1sOkF0dHJpYnV0ZT48c2FtbDpBdHRyaWJ1dGUgQXR0cmlidXRlTmFtZT0ibmFtZSIgQXR0cmlidXRlTmFtZXNwYWNlPSJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcyI+PHNhbWw6QXR0cmlidXRlVmFsdWU+QUZGNEY2MkUzREIwMDAwMTwvc2FtbDpBdHRyaWJ1dGVWYWx1ZT48L3NhbWw6QXR0cmlidXRlPjwvc2FtbDpBdHRyaWJ1dGVTdGF0ZW1lbnQ+PFNpZ25hdHVyZSB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC8wOS94bWxkc2lnIyI+PFNpZ25lZEluZm8+PENhbm9uaWNhbGl6YXRpb25NZXRob2QgQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzEwL3htbC1leGMtYzE0biMiPjwvQ2Fub25pY2FsaXphdGlvbk1ldGhvZD48U2lnbmF0dXJlTWV0aG9kIEFsZ29yaXRobT0iaHR0cDovL3d3dy53My5vcmcvMjAwMC8wOS94bWxkc2lnI3JzYS1zaGExIj48L1NpZ25hdHVyZU1ldGhvZD48UmVmZXJlbmNlIFVSST0iI19mMGM3ZTlkMi1iMThjLTRhNzUtYTEyNS1iMjkzYzIwZDRmYjMiPjxUcmFuc2Zvcm1zPjxUcmFuc2Zvcm0gQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwLzA5L3htbGRzaWcjZW52ZWxvcGVkLXNpZ25hdHVyZSI+PC9UcmFuc2Zvcm0+PFRyYW5zZm9ybSBBbGdvcml0aG09Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvMTAveG1sLWV4Yy1jMTRuIyI+PC9UcmFuc2Zvcm0+PC9UcmFuc2Zvcm1zPjxEaWdlc3RNZXRob2QgQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwLzA5L3htbGRzaWcjc2hhMSI+PC9EaWdlc3RNZXRob2Q+PERpZ2VzdFZhbHVlPlpsS0M5Qi9FUC9nK0hGOGFFUzQ4V3dpejAvWT08L0RpZ2VzdFZhbHVlPjwvUmVmZXJlbmNlPjwvU2lnbmVkSW5mbz48U2lnbmF0dXJlVmFsdWU+bDlaYng5Q25aOE5ab053blYyR1FwMzBVTi93eTBKN2ZOeENianB3Qkw2QUNueU4zMkU2eVBNQWZoZkdrVWljclBHODdVVDNTa3Y5cjVIUkRYY1E2YVJFcWgvUnZ4QmpBY2lIWWVZSnNSa28xc3c0TmdTNGRSa3IwcWhnQm5YdUxiWnowU1llaGJIVlUrWFNPQTVOM0N0ckFkenk3UzY4L1RlWVJBQUl1YzhONXUwSkV2N0NyTHRaSFFZZTluTE5sZW1BZ0wyeUQrQ2hpMmQ0aFBMREdIclJQVHMxMGJYcm1Idm9NZ1dyUUFFWGdUTXBKaENtNndWUU9BbjM4RkhKOUd4OVY3U2RackhGaTJHVlFUeXhCdUhEV1Irb1NmSTJSekxqV2FlTUd6aFpVYnJOMkJXeEN4WnFJdU1aNVMybDZpYzRjZHR3UU5oZ3F2VlVXdFI3QllnPT08L1NpZ25hdHVyZVZhbHVlPjxLZXlJbmZvPjxvOlNlY3VyaXR5VG9rZW5SZWZlcmVuY2UgeG1sbnM6bz0iaHR0cDovL2RvY3Mub2FzaXMtb3Blbi5vcmcvd3NzLzIwMDQvMDEvb2FzaXMtMjAwNDAxLXdzcy13c3NlY3VyaXR5LXNlY2V4dC0xLjAueHNkIj48bzpLZXlJZGVudGlmaWVyIFZhbHVlVHlwZT0iaHR0cDovL2RvY3Mub2FzaXMtb3Blbi5vcmcvd3NzL29hc2lzLXdzcy1zb2FwLW1lc3NhZ2Utc2VjdXJpdHktMS4xI1RodW1icHJpbnRTSEExIj5ZREJlRFNGM0Z4R2dmd3pSLzBwck11OTZoQ2M9PC9vOktleUlkZW50aWZpZXI+PC9vOlNlY3VyaXR5VG9rZW5SZWZlcmVuY2U+PC9LZXlJbmZvPjwvU2lnbmF0dXJlPjwvc2FtbDpBc3NlcnRpb24+"

nab_instance = nabcommerce.Nabcommerce(identity_token)

# -- Load from a previously saved application profile
# print "Loading application_id and token from saved state in config.dat..."
# nab_instance.load
# -- Or do Step 2 Below.


print "\n","********   Step 2 - Managing Application Configuration Data  **********","\n"
# https://my.ipcommerce.com/Docs/1.17.16/CWS_REST_Developer_Guide/RESTImplementation/PreparingTheAppToTransact/ManagingAppConfigData/index.aspx



#The PTLS Id is used to uniquely identify an application.
my_PTLS = "MIIFCzCCA/OgAwIBAgICAoEwDQYJKoZIhvcNAQEFBQAwgbExNDAyBgNVBAMTK0lQIFBheW1lbnRzIEZyYW1ld29yayBDZXJ0aWZpY2F0ZSBBdXRob3JpdHkxCzAJBgNVBAYTAlVTMREwDwYDVQQIEwhDb2xvcmFkbzEPMA0GA1UEBxMGRGVudmVyMRowGAYDVQQKExFJUCBDb21tZXJjZSwgSW5jLjEsMCoGCSqGSIb3DQEJARYdYWRtaW5AaXBwYXltZW50c2ZyYW1ld29yay5jb20wHhcNMTMwODI2MTcxMDI3WhcNMjMwODI0MTcxMDI3WjCBjDELMAkGA1UEBhMCVVMxETAPBgNVBAgTCENvbG9yYWRvMQ8wDQYDVQQHEwZEZW52ZXIxGjAYBgNVBAoTEUlQIENvbW1lcmNlLCBJbmMuMT0wOwYDVQQDEzR0ZHNwM25TZ0FJQUFBUDhBSCtDWUFBQUVBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUFBQUE9MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAtn6ILI78EaOLcWrmI9RZf8Vj+3P/WcrDLimSyJJH/8LnIBbXNkiKcZSMg/KHqNLAtq/ncYqZcicgAfaoSbj9FxKGIXTDEICriv/i8sQIGFhIwW/V6H02E8SpWjdCQO9EUUaFPUVMhHfiabwJ3B0VODsQfVuG7mbrAvD/wAqiUVR2Q0rpgHkToCkytdhMlkXiFtnfy4nnoFnI6c5cmsQU7AZgI6Zr08pDMN9y3uSRGSJIzdcTohBA1qb8C4+ZVRCmwCfQZiBHxjC8c5DTiGlPQVEDfRjKXm6ffqBKCttX7qCeB0s57iob0Q7ucz8NfoWtY8dZVzMhYH8obU/dSXaZ6wIDAQABo4IBTjCCAUowCQYDVR0TBAIwADAdBgNVHQ4EFgQUJ64+T3k9d5nWfplPlxVZsN382XUwgeYGA1UdIwSB3jCB24AU3+ASnJQimuunAZqQDgNcnO2HuHShgbekgbQwgbExNDAyBgNVBAMTK0lQIFBheW1lbnRzIEZyYW1ld29yayBDZXJ0aWZpY2F0ZSBBdXRob3JpdHkxCzAJBgNVBAYTAlVTMREwDwYDVQQIEwhDb2xvcmFkbzEPMA0GA1UEBxMGRGVudmVyMRowGAYDVQQKExFJUCBDb21tZXJjZSwgSW5jLjEsMCoGCSqGSIb3DQEJARYdYWRtaW5AaXBwYXltZW50c2ZyYW1ld29yay5jb22CCQD/yDY5hYVsVzA1BgNVHR8ELjAsMCqgKKAmhiRodHRwOi8vY3JsLmlwY29tbWVyY2UuY29tL2NhLWNybC5jcmwwDQYJKoZIhvcNAQEFBQADggEBAJrku2QD0T/0aT+jfFJA947Vf7Vu/6S1OxUGhMipx6z/izXZ+o4fK/Nsg0G39KvfxippFG/3MUo621dwXwtqq9SM72zy9ry9E0ptmEiG8X8bSVOyGj4MqyExCPs9LgloV5GgewqYRgq2hmbXOv8Gw7EeXGCfnQ+eROxGu1+p3ZWUnGMQnBbayg43npcHYfyLFHOzd57pj6ncYoxY3kun5GLMLr6tJXKpPNvbM5lAOzcAmKviPMCM2T53UzJlsRdVvCbnkrc5cYqN4l01elqr3MSsj6BJ+JqIqViFrYYkD34THKO8c+wZGb8IN+NJAVre9YOvt5+Cvbbd5ik0UQ+YQNM="
appdata = {
	"ApplicationAttended":'false',
	"ApplicationLocation":"4",
	"ApplicationName":'TestApp',
	"HardwareType":"2",
	"PINCapability":"3",
	"PTLSSocketId":my_PTLS,
	"ReadCapability":"2",
	"SerialNumber":"12345",
	"SoftwareVersion":1,
	"SoftwareVersionDate": "%s" % datetime.datetime.now()
}
print "\n","Save Application Data ...\n","Result:\n",
app_id=nab_instance.save_application_data(appdata);
print app_id

print "\n","Get Application Data ...\n","Result:\n",
print nab_instance.get_application_data(app_id);

# -- You may
# nab_instance.delete_application_data(app_id);
#
# This will yield a warning if the current application profile is given.
# pass with (app_id, true) to skip that check.


print "\n","********   Step 3 - Retreiving Service Information  **********\n","\n"
# https://my.ipcommerce.com/Docs/1.17.16/CWS_REST_Developer_Guide/RESTImplementation/PreparingTheAppToTransact/RetrievingServiceInformation.aspx


print "\n","Get Service Information...\n","Result:\n",
workflow_ids=nab_instance.get_service_information();

print "\n","********   Step 4 - Managing Merchant Profiles **********\n","\n"
# https://my.ipcommerce.com/Docs/1.17.16/CWS_REST_Developer_Guide/RESTImplementation/PreparingTheAppToTransact/ManagingMerchantProfiles/index.aspx

# Can be used to reset merchant profiles
#
#
#for svc in workflow_ids:
#	merchant_profiles=nab_instance.get_merchant_profile(nil,default_workflow_id)
#	for profile in merchant_profiles:
#		nab_instance.delete_merchant_profile(profile["id"])
#		
#	
#

for svc in workflow_ids:
	autotest_profile="Merchant_"+svc["ServiceId"]
	
	print "\n","Is Merchant Profile Initialized: "+autotest_profile+" ...","Result:",
	initialized = nab_instance.is_merchant_profile_initialized(autotest_profile, svc["ServiceId"])
	if not initialized:
		merchant_profile={"ProfileId":autotest_profile,"WorkflowId":svc["ServiceId"],
		"ServiceName":svc["ServiceName"],"LastUpdated": "%s" % datetime.datetime.now(),
		"MerchantData":{"CustomerServiceInternet":"","CustomerServicePhone":"303 3333333","Language":127,
		"Address":{"Street1":"777 Cherry Street","Street2":"","City":"Denver","StateProvince":7,
		"PostalCode":"80220","CountryCode":234},"MerchantId":"123456789012","Name":"ABCTest",
		"Phone":"303 3333333","TaxId":"","BankcardMerchantData":{"ABANumber":"1234",
		"AcquirerBIN":"123456","AgentBank":"123456","AgentChain":"1234","Aggregator":False,
		"ClientNumber":"1224","IndustryType":4,"Location":"001","MerchantType":"","PrintCustomerServicePhone":False,
		"QualificationCodes":"","ReimbursementAttribute":"1","SIC":"1234","SecondaryTerminalId":"12345678",
		"SettlementAgent":"1234","SharingGroup":"1234","StoreId":"1234","TerminalId":"123","TimeZoneDifferential":"123"},
		"ElectronicCheckingMerchantData":{"OrginatorId":"","ProductId":"","SiteId":""}},
		"TransactionData":{"BankcardTransactionDataDefaults":{"CurrencyCode":4,"CustomerPresent":1,
		"EntryMode":1,"RequestACI":2,"RequestAdvice":2}}}
		print "\n","Save Merchant Profile: #{autotest_profile} ...","Result:",
		print nab_instance.save_merchant_profile(merchant_profile, svc["ServiceId"]);
	
	print "\n","Get Merchant Profile: #{autotest_profile} ...","Result:",
	print nab_instance.get_merchant_profile(autotest_profile, svc["ServiceId"])



#sure we made sure TestProfile exists, but we will use the first returned.



print "\n","########   Ready to Transact ########\n","\n"
