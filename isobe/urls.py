from controllers import api
from controllers import RootController,JSONController

api.add_route("/",RootController)#htmlを表示させることを行う
api.add_route("/JSON",JSONController)#JSONの情報を取得することを行う
api.add_route("/JSON/id={id}&name={name}&email={email}",JSONController)