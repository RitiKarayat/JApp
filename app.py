from notes import create_app,auth
app  =create_app()

# @auth.route('/login')
# def index():
#     return 'hello'


app.run(host='0.0.0.0',port=5000,debug=True)

