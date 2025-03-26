from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/calculate")
def calculate(a: float, b: float, operation: str):
    if operation == "add":
        return {"result": a + b}
    elif operation == "subtract":
        return {"result": a - b}
    elif operation == "multiply":
        return {"result": a * b}
    elif operation == "divide":
        if b == 0:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed")
        return {"result": a / b}
    else:
        raise HTTPException(status_code=400, detail="Invalid operation. Choose from add, subtract, multiply, divide")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
