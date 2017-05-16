from flask import Flask,request
import json
import requests
app = Flask(__name__)

@app.route('/health')
def health():
    data = {'linkerd':'down','namerd':'down','namerd':'down','linkerd-tcp':'down','linkerd-viz':'down'}
	# linkerd health
    r = requests.get('http://localhost:9990/admin/ping')
    r3 = requests.get('http://localhost:9991/admin/ping')
    r1 = requests.get('http://localhost:9992/metrics')
    r2= requests.get('http://localhost:3000')
    if r.text=="pong":

		data['linkerd'] = 'up'

	# namerd health
	
    if r3.text=="pong":

		data['namerd'] = 'up'

	# linkerd-tcp

	
    if r1.status_code==200:

		data['linkerd-tcp'] = 'up'

	# linkerd-viz
	
    if r2.status_code==200:

		data['linkerd-viz'] = 'up'

		response = app.response_class(response=json.dumps(data),status=200,mimetype='application/json')
    return response

@app.route('/shift',methods = ['GET'])
def balance_traffic():

	N = int(request.args.get('N'))
	headers={}
	path="http://localhost:4180/api/1/dtabs/default"
	balancing=str(100-N)+"*/svc/redis1 & "+str(N)+"*/svc/redis2"
	params=[{"prefix":"/svc","dst":"/#/io.l5d.fs"},{"prefix":"/svc/redis","dst":balancing}]
	headers["Content-Type"] = "application/json"
	response = requests.put(path,data=json.dumps(params),headers=headers)
	print(response.status_code)
	return str(response.status_code)	


@app.route('/',methods = ['GET'])
def welcome():

	return "Welcome to Buoyant Take Home Project"
    
    

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
