from bottle import route,run,template,Bottle,request

app=Bottle()

@app.get('/updateData')
def index():
    return template('template/index.tpl')

@app.post('/updateData')
def postdata():
    name= request.forms.get('name')
    print(name)
    return f'<h1> {name}</h1>'

run(app,host='localhost',port=8080)
