import requests
import json
import ast



	
def getCapital(file_name):
	f = open(file_name+".json","w")
	res ={}
	for country_code in code_to_name:
		r = requests.get("http://api.worldbank.org/countries/%s?format=json" % (country_code))
		try :
			content=json.loads(r.content)
			res[country_code]= content[1][0]["capitalCity"]
		except Exception, e:
			print e

	f.write(json.dumps(res))
	f.close()


	
def getincomeLevel(file_name):
	f = open(file_name+".json","w")
	res ={}
	for country_code in code_to_name:
		r = requests.get("http://api.worldbank.org/countries/%s?format=json" % (country_code))
		try :
			content=json.loads(r.content)
			res[country_code]= content[1][0]["incomeLevel"]["value"]
          
		except Exception, e:
			print e

	f.write(json.dumps(res))
	f.close()
	
    
    
def getIndicator(indicator_code, file_name):
    f = open(file_name+".json","w")
    res ={}
    for country_code in code_to_name:
        r = requests.get("http://api.worldbank.org/countries/%s/indicators/%s?per_page=10&date=2007:2007&format=json" % (country_code,indicator_code))
        try :
            content=json.loads(r.content)
            res[country_code]= content[1][0]["value"]

        except Exception, e:
            print e
      
    f.write(json.dumps(res))
    f.close()


f = open("code_to_name.json")  
code_to_name = f.read()
code_to_name = json.dumps(json.loads(code_to_name)) 	
code_to_name=ast.literal_eval(code_to_name)
getIndicator("SH.DYN.MORT","POP")
getIndicator("NY.GDP.PCAP.CD","GDP")
getincomeLevel("incomeLevel")
getCapital("capital")

