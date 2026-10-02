from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_workflow(): 
    data=client.post("/v1/run",json={"value":"ship feature"}).json()
    assert len(data["steps"])==4
    assert data["checkpoint"]=="verify"
