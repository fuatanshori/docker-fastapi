import FastApi

app = FastApi()

@app.get("/")
def helloWorld():
    return{"message":"hello world"}