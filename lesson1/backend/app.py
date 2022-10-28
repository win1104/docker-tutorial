from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root(name: str):
	# wlchurch
    return {"message": f"Hello {name}"}
