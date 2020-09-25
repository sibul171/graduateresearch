import responder
import json
api=responder.API()
class JSONController:
    async def on_get(self,req,resp):
        json_open=open("test.json",'r')
        json_load=json.load(json_open)
        resp.media=json_load
    async def on_post(self,req,resp,*,id,name,email):
        
        json_post={"id":id,"name":name,"email":email}
        with open("test2.json","w") as f:
            json.dump(json_post,f)
        
class RootController:
    async def on_get(self,req,resp):
        resp.content=api.template("index.html")