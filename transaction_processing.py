import nabcommerce
import datetime
print "See source for links to documentation\n"

identity_token="PHNhbWw6QXNzZXJ0aW9uIE1ham9yVmVyc2lvbj0iMSIgTWlub3JWZXJzaW9uPSIxIiBBc3NlcnRpb25JRD0iX2YwYzdlOWQyLWIxOGMtNGE3NS1hMTI1LWIyOTNjMjBkNGZiMyIgSXNzdWVyPSJJcGNBdXRoZW50aWNhdGlvbiIgSXNzdWVJbnN0YW50PSIyMDE0LTA0LTAyVDE5OjIzOjM1LjExOFoiIHhtbG5zOnNhbWw9InVybjpvYXNpczpuYW1lczp0YzpTQU1MOjEuMDphc3NlcnRpb24iPjxzYW1sOkNvbmRpdGlvbnMgTm90QmVmb3JlPSIyMDE0LTA0LTAyVDE5OjIzOjM1LjExOFoiIE5vdE9uT3JBZnRlcj0iMjAxNy0wNC0wMlQxOToyMzozNS4xMThaIj48L3NhbWw6Q29uZGl0aW9ucz48c2FtbDpBZHZpY2U+PC9zYW1sOkFkdmljZT48c2FtbDpBdHRyaWJ1dGVTdGF0ZW1lbnQ+PHNhbWw6U3ViamVjdD48c2FtbDpOYW1lSWRlbnRpZmllcj5BRkY0RjYyRTNEQjAwMDAxPC9zYW1sOk5hbWVJZGVudGlmaWVyPjwvc2FtbDpTdWJqZWN0PjxzYW1sOkF0dHJpYnV0ZSBBdHRyaWJ1dGVOYW1lPSJTQUsiIEF0dHJpYnV0ZU5hbWVzcGFjZT0iaHR0cDovL3NjaGVtYXMuaXBjb21tZXJjZS5jb20vSWRlbnRpdHkiPjxzYW1sOkF0dHJpYnV0ZVZhbHVlPkFGRjRGNjJFM0RCMDAwMDE8L3NhbWw6QXR0cmlidXRlVmFsdWU+PC9zYW1sOkF0dHJpYnV0ZT48c2FtbDpBdHRyaWJ1dGUgQXR0cmlidXRlTmFtZT0iU2VyaWFsIiBBdHRyaWJ1dGVOYW1lc3BhY2U9Imh0dHA6Ly9zY2hlbWFzLmlwY29tbWVyY2UuY29tL0lkZW50aXR5Ij48c2FtbDpBdHRyaWJ1dGVWYWx1ZT5hZDQwMWQ1Yy1hNzZmLTRlYWItYmU5ZC1mNjU2NjlmOWE0ZTg8L3NhbWw6QXR0cmlidXRlVmFsdWU+PC9zYW1sOkF0dHJpYnV0ZT48c2FtbDpBdHRyaWJ1dGUgQXR0cmlidXRlTmFtZT0ibmFtZSIgQXR0cmlidXRlTmFtZXNwYWNlPSJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcyI+PHNhbWw6QXR0cmlidXRlVmFsdWU+QUZGNEY2MkUzREIwMDAwMTwvc2FtbDpBdHRyaWJ1dGVWYWx1ZT48L3NhbWw6QXR0cmlidXRlPjwvc2FtbDpBdHRyaWJ1dGVTdGF0ZW1lbnQ+PFNpZ25hdHVyZSB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC8wOS94bWxkc2lnIyI+PFNpZ25lZEluZm8+PENhbm9uaWNhbGl6YXRpb25NZXRob2QgQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAxLzEwL3htbC1leGMtYzE0biMiPjwvQ2Fub25pY2FsaXphdGlvbk1ldGhvZD48U2lnbmF0dXJlTWV0aG9kIEFsZ29yaXRobT0iaHR0cDovL3d3dy53My5vcmcvMjAwMC8wOS94bWxkc2lnI3JzYS1zaGExIj48L1NpZ25hdHVyZU1ldGhvZD48UmVmZXJlbmNlIFVSST0iI19mMGM3ZTlkMi1iMThjLTRhNzUtYTEyNS1iMjkzYzIwZDRmYjMiPjxUcmFuc2Zvcm1zPjxUcmFuc2Zvcm0gQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwLzA5L3htbGRzaWcjZW52ZWxvcGVkLXNpZ25hdHVyZSI+PC9UcmFuc2Zvcm0+PFRyYW5zZm9ybSBBbGdvcml0aG09Imh0dHA6Ly93d3cudzMub3JnLzIwMDEvMTAveG1sLWV4Yy1jMTRuIyI+PC9UcmFuc2Zvcm0+PC9UcmFuc2Zvcm1zPjxEaWdlc3RNZXRob2QgQWxnb3JpdGhtPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwLzA5L3htbGRzaWcjc2hhMSI+PC9EaWdlc3RNZXRob2Q+PERpZ2VzdFZhbHVlPlpsS0M5Qi9FUC9nK0hGOGFFUzQ4V3dpejAvWT08L0RpZ2VzdFZhbHVlPjwvUmVmZXJlbmNlPjwvU2lnbmVkSW5mbz48U2lnbmF0dXJlVmFsdWU+bDlaYng5Q25aOE5ab053blYyR1FwMzBVTi93eTBKN2ZOeENianB3Qkw2QUNueU4zMkU2eVBNQWZoZkdrVWljclBHODdVVDNTa3Y5cjVIUkRYY1E2YVJFcWgvUnZ4QmpBY2lIWWVZSnNSa28xc3c0TmdTNGRSa3IwcWhnQm5YdUxiWnowU1llaGJIVlUrWFNPQTVOM0N0ckFkenk3UzY4L1RlWVJBQUl1YzhONXUwSkV2N0NyTHRaSFFZZTluTE5sZW1BZ0wyeUQrQ2hpMmQ0aFBMREdIclJQVHMxMGJYcm1Idm9NZ1dyUUFFWGdUTXBKaENtNndWUU9BbjM4RkhKOUd4OVY3U2RackhGaTJHVlFUeXhCdUhEV1Irb1NmSTJSekxqV2FlTUd6aFpVYnJOMkJXeEN4WnFJdU1aNVMybDZpYzRjZHR3UU5oZ3F2VlVXdFI3QllnPT08L1NpZ25hdHVyZVZhbHVlPjxLZXlJbmZvPjxvOlNlY3VyaXR5VG9rZW5SZWZlcmVuY2UgeG1sbnM6bz0iaHR0cDovL2RvY3Mub2FzaXMtb3Blbi5vcmcvd3NzLzIwMDQvMDEvb2FzaXMtMjAwNDAxLXdzcy13c3NlY3VyaXR5LXNlY2V4dC0xLjAueHNkIj48bzpLZXlJZGVudGlmaWVyIFZhbHVlVHlwZT0iaHR0cDovL2RvY3Mub2FzaXMtb3Blbi5vcmcvd3NzL29hc2lzLXdzcy1zb2FwLW1lc3NhZ2Utc2VjdXJpdHktMS4xI1RodW1icHJpbnRTSEExIj5ZREJlRFNGM0Z4R2dmd3pSLzBwck11OTZoQ2M9PC9vOktleUlkZW50aWZpZXI+PC9vOlNlY3VyaXR5VG9rZW5SZWZlcmVuY2U+PC9LZXlJbmZvPjwvU2lnbmF0dXJlPjwvc2FtbDpBc3NlcnRpb24+"

nab_instance=nabcommerce.Nabcommerce(identity_token)

#This value is received from a one-time call to save_application_data()
#The value is linked to your PTLS Socket Id, and will not change after initial setup.

nab_instance.application_id="2696"
workflow_ids=nab_instance.get_service_information();

for svc in workflow_ids:
	autotest_profile="Merchant_"+svc["ServiceId"]
	initialized=nab_instance.is_merchant_profile_initialized(autotest_profile, svc["ServiceId"])

	if initialized: g="true"
	else: g="false"
	print svc, "\nInitialization check:"+g,"\n"
	if not initialized:
		merchantProfile={"ProfileId":"autotest_profile","ServiceName":svc["ServiceName"],"LastUpdated":"%s" %datetime.datetime.today(),"MerchantData":{"CustomerServiceInternet":"","CustomerServicePhone":"303 3333333","Language":"127","Address":{"Street1":"777 Cherry Street","Street2":"","City":"Denver","StateProvince":"7","PostalCode":"80220","CountryCode":"234"},"MerchantId":"123456789012","Name":"ABCTest","Phone":"303 3333333","TaxId":"","BankcardMerchantData":{"ABANumber":"1234","AcquirerBIN":"123456","AgentBank":"123456","AgentChain":"123456","Aggregator":False,"ClientNumber":"1224","IndustryType":"4","Location":"000","MerchantType":"","PrintCustomerServicePhone":False,"QualificationCodes":"","ReimbursementAttribute":"1","SIC":"1234","SecondaryTerminalId":"12345678","SettlementAgent":"1234","SharingGroup":"1234","StoreId":"1234","TerminalId":"124","TimeZoneDifferential":"123"},"ElectronicCheckingMerchantData":{"OrginatorId":"","ProductId":"","SiteId":""}},"TransactionData":{"BankcardTransactionDataDefaults":{"CurrencyCode":"4","CustomerPresent":"1","EntryMode":"0","RequestACI":"2","RequestAdvice":"2"}}}
		nab_instance.save_merchant_profile(merchantProfile, svc["ServiceId"])
		
#sure we made sure TestProfile exists, but we will use the first returned.

txndata={"CustomerData":None,"ReportingData":None,"Addendum":None,"ApplicationConfigurationData":None,
"TenderData":{"PaymentAccountDataToken":None,"SecurePaymentAccountData":None,"CardData":{"CardType":"3",
"CardholderName":None,"PAN":5454545454545454,"Expire":1210,"Track1Data":None,"Track2Data":None},
"CardSecurityData":{"AVSData":{"CardholderName":"SJohnson","Street":"777 Cherry Street","City":"Denver",
"StateProvince":"CO","PostalCode":"80220","Country":"234","Phone":None},"CVDataProvided":"2","CVData":"123",
"KeySerialNumber":None,"PIN":None},"EcommerceSecurityData":None},"TransactionData":{"Amount":"10.00",
"CurrencyCode":"4","TransactionDateTime":datetime.datetime.today(),"AccountType":"0","AlternativeMerchantData":None,
"ApprovalCode":None,"CashBackAmount":"0.00","CustomerPresent":"0","EmployeeId":"12345","EntryMode":"1",
"GoodsType":"2","IndustryType":"4","InternetTransactionData":{"IpAddress":"1.1.1.1","SessionId":"12345"},
"InvoiceNumber":None,"OrderNumber":"12345","IsPartialShipment":False,"SignatureCaptured":False,
"TerminalId":None,"LaneId":"99","TipAmount":"0.00","BatchAssignment":None}}
#https://my.ipcommerce.com/Docs/1.17.15/CWS_API_Reference/BaseTxnDataElements/Transaction.aspx

tokenized_txn=None
capture_selective_txn=None
basic_txn=None
captured_txn_to_return=None

for svc in workflow_ids:
	profile="Merchant_"+svc["ServiceId"]
	workflow_id=svc["ServiceId"]
	
	if (svc["Operations"]["AuthAndCapture"]):
		if (svc["Tenders"]["CreditAuthorizeSupport"]==2):
			print "\n","\n","Begin Authorize and Capture with WorkflowId: ",workflow_id
			print "Result:",
			nab_instance.authorize_and_capture(txndata, profile, workflow_id)

	if (svc["Operations"]["Authorize"]):
		print "\n","\n","Begin Authorize with WorkflowId: ",workflow_id
		print "Result:",
		basic_txn=nab_instance.authorize(txndata,profile, workflow_id)

	if (svc["Operations"]["Authorize"]):
		print "\n","\n","Begin Authorize with WorkflowId: ",workflow_id
		print "Result:",
		capture_selective_txn=nab_instance.authorize(txndata,profile, workflow_id)

	if (svc["Operations"]["Authorize"] and capture_selective_txn != None):
		payment_token=capture_selective_txn["PaymentAccountDataToken"]
		txndata_tokenized=dict(txndata)
		txndata_tokenized['CardData']=None
		txndata_tokenized['PaymentAccountDataToken']=payment_token
		
		
		print "\n","\n","Begin Tokenized Authorize with WorkflowId: #{workflow_id} templating from previous transaction."
		print "Result:",
		tokenized_txn=nab_instance.authorize(txndata_tokenized, profile, workflow_id)

	if (svc["Operations"]["Capture"] and basic_txn != None):
		print "\n","\n","Begin Capture with WorkflowId: ",workflow_id
		print "Result:",
		captured_txn=nab_instance.capture(basic_txn["TransactionId"],{"Amount":"24.00", "TipAmount":"4.00"},  profile, workflow_id)

	if (svc["Operations"]["Capture"] and tokenized_txn != None):
		print "\n","\n","Begin Tokenized Capture with WorkflowId: ",workflow_id
		print "Result:",
		captured_txn_to_return=nab_instance.capture(tokenized_txn["TransactionId"],{"Amount":"20.00"},  profile, workflow_id)

	if (svc["Operations"]["CaptureSelective"] and capture_selective_txn!= None):
		print "\n","\n","Begin Capture Selective with WorkflowId: ",workflow_id
		print "Result:",
		captured_txns=nab_instance.capture_selective(profile, workflow_id, [capture_selective_txn["TransactionId"]])
		captured_txn_to_return=capture_selective_txn

	if (svc["Operations"]["CaptureAll"] and basic_txn!=None and svc["Tenders"]["BatchAssignmentSupport"] != 3):
		print "\n","\n","Begin Capture All with WorkflowId: ",workflow_id
		print "Result:",
		captured_txns=nab_instance.capture_all(profile, workflow_id)

	if (svc["Operations"]["ReturnById"] and captured_txn_to_return!= None):
		print "\n","\n","Begin ReturnById with WorkflowId: ",workflow_id
		print "Result:",
		nab_instance.return_by_id(captured_txn_to_return["TransactionId"],{"Amount":"5.00"},  profile, workflow_id)
	
print "\n","\n","Completed Test."
