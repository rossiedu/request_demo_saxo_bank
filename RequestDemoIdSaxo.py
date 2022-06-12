from zeep import Client
from zeep import xsd
from random import randint

def GenerateDemoId(Nome):
  wsdl = 'http://mitsweb.iitech.dk/PPSSWS/PartnerRegistrationWebservice/RegistrationWS.asmx?wsdl'
  client = Client(wsdl = 'http://mitsweb.iitech.dk/PPSSWS/PartnerRegistrationWebservice/RegistrationWS.asmx?wsdl')
  ownerID = ownerid
  profileGuid = 'profileGuid'
  ownerPassword = 'password'
  ClientPW = f'P{(randint((10**(6-1)), ((10**6)-1)))}'
  with client.settings(raw_response=True):
    response = client.service.RegisterUserWithAutoId(ownerID,profileGuid,ownerPassword,Nome,ClientPW)
  assert response.status_code == 200
  assert response.content 
  responseBytes =response.content
  encoding = 'utf-8'
  response = responseBytes.decode(encoding)
  sLogin = response.find("clientid=")+len('clientid=')+1
  eLogin = sLogin +8
  login = response[sLogin:eLogin]
  return f'{login},{ClientPW}'