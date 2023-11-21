from neuroscope.main import create_app
from neuroscope.config import DevConfig, ProdConfig

app = create_app(DevConfig)

#run with 
if __name__ == "__main__":
    app.run()

'''
from neuroscope.controller import app, db
#app.init_app()

if __name__ == "__main__":
    with app.app_context():
       db.create_all()
    app.run(debug=True, host='127.0.0.1', port=5001)
'''