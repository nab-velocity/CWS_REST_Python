import httplib
import logging
import json
import datetime
import time
import base64
import marshal

import error

class Nabcommerce():
	URL = 'api.cert.nabcommerce.com'
	ENDPOINT='/REST/2.0.18'
	TMS_REST_SCHEMA=",http://schemas.ipcommerce.com/CWS/v2.0/DataServices/TMS/Rest"
	TXN_REST_SCHEMA=",http://schemas.ipcommerce.com/CWS/v2.0/Transactions/Rest"
	
	def __init__ (self, identity_token):
		self.identity_token=identity_token
		self.application_id=""
		self.session_token=""
		self.profile_id=""
		self.revalidate=True
		self.ready_state=0
		self.renew_time=0
		
		self.identity_token=identity_token
		
		print "Trying to sign on..."
		self.__sign_on_with_token();
		in_where="to nabcommerce constructor"
		
		if not self.__validate_session():
			if self.ready_state==0:
				error= "Please provide a valid identity token "+ in_where +"."
			else:
				error= "Please ensure the identity token provided "+ in_where+ " is valid."
			raise self.IpcError, error
		
		
	def __sign_on_with_token(self):
		self.ready_state=0
		self.renew_time=0
		self.session_token=self.identity_token
		#print "Signing on..."
		self.session_token=self.__tokenized_action("GET","SvcInfo/token")
		if (self.session_token!=None): self.ready_state=1
		#We can now check if an identity token was returned.
		if (self.__validate_session()):
			return True #print "Done",""; true
		else:
			return False
			#print "Failed",""; false
	
	
	def __validate_session(self, revalidate=None):
		#Setting ready_state to zero prevents any automatic signons, and all subsequent calls to
		#print "validate_session", revalidate
		if revalidate==None:
			revalidate=self.revalidate
		if self.ready_state==1:
			# A session token lasts thirty minutes.
			# The ruby implementation reads the session token, and gets the 
			# Expiration directly. This can be done by xmlparsing the base64 decoded saml token.
			self.renew_time=time.time()+1500 # 25 minutes to be safe
			
			self.ready_state=2
			print "Session saved"
		elif (self.ready_state>=2):
			if (self.renew_time <= time.time()):
				if not revalidate:
					return False
				if (self.renew_time > time.time()):
					print "Expired session was renewed by another process."
					return True;
				print "Expired session will be renewed."
				self.__sign_on_with_token()
		else:
			return False
		return True

	def __tokenized_action(self, method, path, body=None, isoDate=False):
	
		conn= httplib.HTTPSConnection(self.URL)
		if body != None:
			if isoDate:
				dthandler = lambda obj: obj.isoformat() if isinstance(obj, datetime.datetime) else None
			else:
				dthandler = lambda obj: "/Date("+str(int(time.mktime(obj.timetuple())))+"000)/" if isinstance(obj, datetime.datetime) else None
			body=json.dumps(body, default=dthandler, sort_keys=True)
			#body=body.replace("$type", "__type");
			# Unforunately this is the most concise solution for ensuring __type is the first 
			# element within the json body of a transaction.
		
		headers=self.__header()


		conn.set_debuglevel(1)
		conn.request(method, self.ENDPOINT+"/"+path, body, headers)
		print "conn.request(",method,", ",self.ENDPOINT+"/"+path,", ",body,",...)"
		
		response=conn.getresponse()
		
		if str(response.status)[0] != "2":
			print response.status, response.reason, response.read()
			return None
		
		response=response.read()
		#print response
		if response[0] == "\"":
			return response[1:-1] #remove quotes
		if response[0] == "{" or response[0] == "[":
			return json.loads(response)
		elif response[0] == "<":
			raise self.NabError("An xml error was passed.\n"+response)
		else:
			return response
		return None
	
	def __header(self):
		
		#required
		#if a non empty Accept header is sent, 
		#NAB server will send a text/xml response.
		authstring=base64.b64encode(self.session_token+":")
		
		return {"Authorization":"Basic "+authstring, "Content-Type": "application/json"}
	
		
	########################################################################
	#"""					BEGIN SERVICE INFO							"""#
	########################################################################
	def get_application_data(self, application_id=None, save=False):
		if not self.__validate_session():
			return False;
			
		self.application_id=application_id
		
		#print "Getting applicaton data for #{application_id}..."
		application_data=self.__tokenized_action("GET", "SvcInfo/appProfile/"+application_id)
		#if not error
		#print "Result:",application_data,"Done"
		if save:
			self.application_id=application_id
		return application_data
	
	
	#Requires application_data which contains an xml 
	
#This value is received from a one-time call to save_application_data()
#The value is linked to your PTLS Socket Id, and will not change after initial setup.
	def save_application_data(self, application_data):
		
		if not self.__validate_session():
			return False
		
		#print "Saving applicaton data..."
		result=self.__tokenized_action("PUT", "SvcInfo/appProfile", application_data)
		#print "Result:" + result

		self.application_id=result["id"]
		#print "Done"
		return self.application_id
	
	
	def delete_application_data(self, application_id=0, force=False):
		if not self.__validate_session():
			return False;
		if (self.application_id==application_id and not force):
			#print "Possible accidental deletion of current running application prevented.","Call delete_application_data(#{application_id}, true) to override."
			return
		
		#print "Deleting applicaton profile..."
		if not self.__tokenized_action("DELETE", "SvcInfo/appProfile/"+application_id):
			return False
		#print "Done"
		
		if (self.application_id==application_id):
			self.application_id=None;
		return application_id
	
	
	#Complete 8/29/11 09:12
	def get_service_information(self):
		
		if not self.__validate_session():
			return False;
		
		#print "Getting service information..."
		
		services=self.__tokenized_action("GET","SvcInfo/serviceInformation")["BankcardServices"]
		
		services_list=[];
		for svc in services:
			services_list.append(self.service_name(svc["ServiceId"])+" ("+svc["ServiceId"]+")")
		
		print len(services)," Service(s) returned: ", ",".join(services_list)
		#print "Result:",services
		
		#print "Done",None
		return services
		
	
	#Works 8/29/11 09:12
	def service_name(self, service_id):
			#Sandbox
		list={"214DF00001": "Chase Paymentech Orbital - Tampa",
		"B51E100001": "Chase Paymentech Orbital - Salem",
		"7B62B00001": "First Data - Nashville",
		"786F400001": "Chase Paymentech Orbital - Tampa Retail",
		"A656D00001": "First Data - Nashville US",
		"4CACF00001": "Chase Tampa Direct TCS",
		"3E2DE00001": "RBS Global Gateway",
		"832E400001": "RBS Worldpay",
		"C82ED00001": "TSYS Sierra",
		"5A38100001": "Tampa - Canada",
		"71C8700001": "TSYS Sierra Canada",
		"8335000001": "TSYS Summit",
		"A4F2B00001": "Salem Direct",
		"E4FB800001": "First Data - Nashville",
		"16E5800001": "Intuit QBMS",
		"A8CFF00001": "First Data BUYPASS",
		"36EBE00001": "Tampa TCS for Canada",
		"6429C00001": "Intuit QBMS Inline Tokenization",
		"8046100001": "Intuit QBMS No Tokenization",
		"207CE00001": "Adaptive Payments",
		"88D9300001": "Fifth Third Payment Services FTPS",
		"8077500001": "Intuit QBMS Inline Tokenization",
		"B447F00001": "Fifth Third Payment Services FTPS",
		"D806000001": "Vantiv IBM",
		"4365400001": "Vantiv Tandem",
		#Production
		"C97EF1300C": "Chase Paymentech Orbital - Tampa",
		"8A4B91300C": "Chase Paymentech Orbital - Salem",
		"19F161300C": "First Data - Nashville",
		"3257B1300C": "Chase Paymentech Orbital - Tampa Retail",
		"859AC1300C": "First Data - Nashville US",
		"633511300C": "Chase Tampa Direct TCS",
		"355931300C": "RBS Global Gateway",
		"8CEA11300C": "RBS Worldpay",
		"168511300C": "TSYS Sierra",
		"852BB1300C": "Tampa - Canada",
		"507BF1300C": "TSYS Sierra Canada",
		"55C3C1300C": "TSYS Summit",
		"D1DDF1300C": "Salem Direct",
		"D917B1300C": "First Data - Nashville",
		"7AC431300C": "Intuit QBMS",
		"7B4DD1300C": "First Data BUYPASS",
		"9461F1300C": "Tampa TCS for Canada",
		"CE4AE1300C": "Intuit QBMS Inline Tokenization",
		"E7DFB1300C": "Intuit QBMS No Tokenization",
		"CAFF61300C": "Adaptive Payments",
		"9999999999": "Fifth Third Payment Services FTPS" #To be implemented
		}
		try:
			return list[service_id]
		except KeyError:
			return "Service Id: "+service_id
	#Requires merchant_profile which is an xml string or object implementing to_s()
	#The rest endpoint can accept multiple merchant_profiles, however this function
	#implements save_merchant_profiles for one profile for improved clarity.
	
	def save_merchant_profile(self, merchant_profile, serviceId=None):
		
		return self.save_merchant_profiles([merchant_profile], serviceId)
	
	def save_merchant_profiles(self, merchant_profiles, serviceId=None):
		if not self.__validate_session():
			return False
		
		#print "Saving merchant profiles..."
		returnVal=self.__tokenized_action("PUT", "SvcInfo/merchProfile?serviceId="+serviceId,merchant_profiles)
		
		return returnVal
		
		#print "Done"
		#JSON.parse(returnVal)
	
	def is_merchant_profile_initialized(self, merchant_profile_id, serviceId=None):
		if not self.__validate_session():
			return False
		
		#print "Checking if merchant profile is initialized..."
		returnVal=self.__tokenized_action("GET", "SvcInfo/merchProfile?serviceId="+serviceId)
		#print "Result:",returnVal
		
		#print "Done"
		return returnVal=="true"
	
	def get_merchant_profile(self, merchant_profile_id=None, serviceId=None):
		if not self.__validate_session():
			return False
		
		#print "Getting merchant profile..."
		if (merchant_profile_id==None):
			merchant_profile=self.__tokenized_action("GET", "SvcInfo/merchProfile?serviceId="+serviceId)
		else:
			merchant_profile=self.__tokenized_action("GET", "SvcInfo/merchProfile/"+merchant_profile_id+"?serviceId="+serviceId)
		#print "Result:",merchant_profile
		
		#print "Done"
		return merchant_profile

	
	def delete_merchant_profile(self, merchant_profile_id, serviceId=None):
		if type(merchant_profile_id)=="Dict":
			merchant_profile_id=merchant_profile_id["ProfileId"]
			
		if not self.__validate_session():
			return False
		
		#print "Deleting merchant profile..."
		merchant_profile=self.__action_with_token("DELETE", "merchProfile",{
			"target":merchant_profile_id,
			"serviceId":serviceId
			})
		return merchant_profile
	########################################################################
	#"""				BEGIN TRANSACTION PROCESSING					"""#
	########################################################################


	def authorize_and_capture(self, transaction, merchant_profile_id=None, workflow_id=None):
		if merchant_profile_id == None:
			merchant_profile_id=self.merchant_profile_id
		if workflow_id == None:
			workflow_id=self.workflow_id
			
		
		request={
			"$type": "AuthorizeAndCaptureTransaction"+self.TXN_REST_SCHEMA,
            "SessionToken": self.session_token,
			"ApplicationProfileId": self.application_id,
			"MerchantProfileId": merchant_profile_id,
			"Transaction": {
				"$type": "BankcardTransaction,http://schemas.ipcommerce.com/CWS/v2.0/Transactions/Bankcard"
			}
		}
		print "\n\n",request
		#transaction["TransactionData"]["TransactionDateTime"]=transaction["TransactionData"]["TransactionDateTime"]
		request["Transaction"].update(transaction)
		print "\n\n",request

		#print request
		if not self.__validate_session():
			return False
		
		print "Submitting authorize and capture..."

		response=self.__tokenized_action("POST","Txn/"+workflow_id,request, True)
		print "Done"
		print response
		return response
	
	def authorize(self, transaction, merchant_profile_id=None, workflow_id=None):
		if merchant_profile_id == None:
			merchant_profile_id=self.merchant_profile_id
		if workflow_id == None:
			workflow_id=self.workflow_id
			
		request={
			"$type": "AuthorizeTransaction"+self.TXN_REST_SCHEMA,
            "SessionToken": self.session_token,
			"ApplicationProfileId": self.application_id,
			"MerchantProfileId": merchant_profile_id,
			"Transaction": {
				"$type": "BankcardTransaction,http://schemas.ipcommerce.com/CWS/v2.0/Transactions/Bankcard"
			}
		}
		request["Transaction"].update(transaction)
		print request
		#print request
		if not self.__validate_session():
			return False
		
		print "Submitting authorize..."
		response=self.__tokenized_action("POST","Txn/"+workflow_id,request, True)
		print "Done"
		print response
		return response
	
	def adjust(self, transaction_id, tip=0, workflow_id=None):
		if workflow_id == None:
			workflow_id=self.workflow_id
			
		request={
			"$type": "Adjust"+self.TXN_REST_SCHEMA,
			"ApplicationProfileId": self.application_id,
			"DifferenceData":{
				"$type": "Adjust,http://schemas.ipcommerce.com/CWS/v2.0/Transactions",
				"TransactionId": transaction_id,
				"TipAmount": tip,
				"Addendum": None,
				"PINDebitReason": 0,
				"TenderData": None
			}
		}
		print request
		if not self.__validate_session():
			return False
		
		print "Submitting adjust..."
		response=self.__tokenized_action("PUT","Txn/"+workflow_id,request, True)
		print "Done"
		return response
	
	def undo(self, transaction_id,workflow_id):
		if workflow_id == None:
			workflow_id=self.workflow_id
			
		
		request={
			"$type": "Undo"+self.TXN_REST_SCHEMA,
			"ApplicationProfileId": self.application_id,
			"DifferenceData":{
				"$type": "BankcardUndo,http://schemas.ipcommerce.com/CWS/v2.0/Transactions/Bankcard",
				"TransactionId": transaction_id,
				"Addendum": None,
				"PINDebitReason": 0,
				"TenderData": None
			}
		}
		print request
		if not self.__validate_session():
			return False
		
		print "Submitting undo..."
		response=self.__tokenized_action("PUT","Txn/"+workflow_id,request, True)
		print "Done"
		print response
		return response
	
	#WORKS
	def capture(self, transaction_id, diff_data, merchant_profile_id, workflow_id):
		request={
			"$type": "Capture"+self.TXN_REST_SCHEMA,
			"ApplicationProfileId": self.application_id,
			"DifferenceData":{
				"$type": "BankcardCapture,http://schemas.ipcommerce.com/CWS/v2.0/Transactions/Bankcard",
				"TransactionId": transaction_id,
				"Addendum": None
			}
		}
		
		request["DifferenceData"].update(diff_data)
		#print request
		if not self.__validate_session():
			return False
		
		print "Submitting capture..."
		
		response=self.__tokenized_action("PUT","Txn/"+workflow_id+"/"+transaction_id,request, True)
		print "Done"
		print response
		return response
	
	def capture_selective(self, merchant_profile_id, workflow_id, transaction_ids, difference_data=[]):
		request={
			"$type": "CaptureSelective"+self.TXN_REST_SCHEMA,
			"ApplicationProfileId": self.application_id,
			"TransactionIds":transaction_ids,
			"DifferenceData":difference_data
		}
		#print request
		if not self.__validate_session():
			return False
		
		print "Submitting capture selective..."
		
		response=self.__tokenized_action("PUT","Txn/"+workflow_id,request, True)
		print "Done"
		print response
		return response
		
	
	def capture_all(self, merchant_profile_id, workflow_id):
		
		request={
			"$type": "CaptureAll"+self.TXN_REST_SCHEMA,
			"ApplicationProfileId": self.application_id,
			"BatchIds": [],
			"MerchantProfileId":merchant_profile_id
		}
		#print request
		if not self.__validate_session():
			return False
		
		print "Submitting capture all..."
		response=self.__tokenized_action("PUT","Txn/"+workflow_id,request, True)
		print "Done"
		print response
		return response
	
	def return_by_id(self, transaction_id, diff_data, merchant_profile_id, workflow_id):
		request={
			"$type": "ReturnById"+self.TXN_REST_SCHEMA,
			"ApplicationProfileId": self.application_id,
			"MerchantProfileId": merchant_profile_id,
			"DifferenceData":{
				"$type": "BankcardReturn,http://schemas.ipcommerce.com/CWS/v2.0/Transactions/Bankcard",
				"TransactionId": transaction_id,
				"Addendum": None
			}
		}
		request["DifferenceData"].update(diff_data)
		#print request
		if not self.__validate_session():
			return False
		
		print "Submitting return by id..."
		response=self.__tokenized_action("POST","Txn/"+workflow_id,request, True)
		print "Done"
		print response
		return response
	
	# Use extreme caution when using this.
	def return_unlinked(self, transaction, merchant_profile_id, workflow_id):
		request={
			"$type":"ReturnTransaction"+self.TXN_REST_SCHEMA,
			"ApplicationProfileId":self.application_id,
			"MerchantProfileId":merchant_profile_id,
			"Transaction":{"$type":"BankcardTransaction,http://schemas.ipcommerce.com/CWS/v2.0/Transactions/Bankcard"}
		}
		request["Transaction"].update(transaction)

		#print request
		if not self.__validate_session():
			return False
		
		#print "Submitting return unlinked..."
		response=self.__tokenized_action("POST","Txn/"+workflow_id,request, True)
		#print "Done"
		#print response
		return response
	
	########################################################################
	#"""				BEGIN TRANSACTION MANAGEMENT					"""#
	########################################################################

	def query_transactions_families(self, args={}):
		options={"capture_states":[0,1,2],"is_acknowledged":0,"query_type":1,
			"start_date":datetime.datetime.now()-datetime.timedelta(1,0),"end_date":datetime.datetime.now(),"page":0,"page_size":50}
		
		options.update(args)
		
		request={
			"$type": "QueryTransactionsFamilies"+self.TMS_REST_SCHEMA,
			"PagingParameters":{
				"$type": "PagingParameters:http://schemas.ipcommerce.com/CWS/v2.0/DataServices",
				"Page":0,
				"PageSize":50,
			},
			"QueryTransactionsParameters":{
				"$type": "QueryTransactionsParameters:http://schemas.ipcommerce.com/CWS/v2.0/DataServices/TMS",
				"CaptureStates":options["capture_states"],
				"IsAcknowledged":options["is_acknowledged"],
				"QueryType":options["query_type"],
				"TransactionDateRange":{
					"EndDateTime":options["end_date"],
					"StartDateTime":options["start_date"]
				}
			}
		}
		#print request
		if not self.__validate_session():
			return False
		
		#print "Submitting Query Transactions Families..."
		
		response=self.__tokenized_action("POST","DataServices/TMS/transactionsFamily", request)
		#print "Done"
		#print response
		return response
	
	def query_batch(self, args={}):
		options={"start_date":datetime.datetime.now()-datetime.timedelta(1,0),
			"end_date":datetime.datetime.now(), "page":0,"page_size":50}
		options.update(args)
		
		
		
		request={
			"$type": "QueryBatch"+self.TMS_REST_SCHEMA,
			"PagingParameters":{
				"$type": "PagingParameters:http://schemas.ipcommerce.com/CWS/v2.0/DataServices",
				"Page":options["page"],
				"PageSize":options["page_size"]
			},
			"QueryBatchParameters":{
				"$type": "QueryBatchParameters:http://schemas.ipcommerce.com/CWS/v2.0/DataServices/TMS",
				"BatchDateRange":{
					"EndDateTime":options["end_date"],
					"StartDateTime":options["start_date"]
				}
			}
		}
		#print request
		if not self.__validate_session():
			return False
		
		#print "Submitting Query Batch..."
		
		response=self.__tokenized_action("POST", "DataServices/TMS/batch", request)
		#print "Done"
		#print response
		return response
	
	def query_transactions_summary(self, args={}):
		options={"capture_states":[1],"is_acknowledged":0,"query_type":1,
			"start_date":datetime.datetime.now()-datetime.timedelta(1,0),"end_date":datetime.datetime.now(),"page":0,"page_size":50}
		
		options.update(args)
		
		
		request={
			"$type": "QueryTransactionsSummary"+self.TMS_REST_SCHEMA,
			"PagingParameters":{
				"$type": "PagingParameters:http://schemas.ipcommerce.com/CWS/v2.0/DataServices",
				"Page":options["page"],
				"PageSize":options["page_size"]
			},
			"QueryTransactionsParameters":{
				"$type": "QueryTransactionsParameters:http://schemas.ipcommerce.com/CWS/v2.0/DataServices/TMS",
				"CaptureStates":options["capture_states"],
				"IsAcknowledged":options["is_acknowledged"],
				"QueryType":options["query_type"],
				"TransactionDateRange":{
					"EndDateTime":options["end_date"],
					"StartDateTime":options["start_date"]
				}
			}
		}
		#print request
		if not self.__validate_session():
			return False
		
		#print "Submitting Query Transactions Summary..."
		
		response=self.__tokenized_action("POST","DataServices/TMS/transactionsSummary",request)
		#print "Done"
		#print response
		return response;
	
	def query_transactions_detail(self, transaction_ids, args={}):
		options={"include_related":0,"is_acknowledged":0,"query_type":1,
			"start_date":datetime.datetime.now()-datetime.timedelta(1,0),"end_date":datetime.datetime.now(),"page":0,"page_size":50}
		
		options.update(args)
		
		
		
		request={
			"$type": "QueryTransactionsDetail"+self.TMS_REST_SCHEMA,
			"PagingParameters":{
				"$type": "PagingParameters:http://schemas.ipcommerce.com/CWS/v2.0/DataServices",
				"Page":options["page"],
				"PageSize":options["page_size"]
			},
			"IncludeRelated":options["include_related"],
			"QueryTransactionsParameters":{
				"$type": "QueryTransactionsParameters:http://schemas.ipcommerce.com/CWS/v2.0/DataServices/TMS",
				"IsAcknowledged":options["is_acknowledged"],
				"QueryType":options["query_type"],
				"TransactionIds":transaction_ids
			},
			"TransactionDetailFormat":2
		}
		#print request
		if not self.__validate_session():
			return False
		
		#print "Submitting Query Transactions Detail..."
		
		response=self.__tokenized_action("POST","DataServices/TMS/transactionsDetail",request)
		#print "Done"
		#print response
		return response