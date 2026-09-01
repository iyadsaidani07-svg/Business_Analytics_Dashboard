from fastapi.testclient import TestClient
from app.api import app
client=TestClient(app)
def test_health_endpoint():
    response=client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status":"ok"}
def test_valid_csv_file():
    csv_content = """Quantity Sold,Unit Price,Sales Amount,Product Category,Region,Sale Date
      2,10,20,A,North,2025-01-01 
      3,20,60,B,South,2025-01-02 """
    response=client.post("/upload",files={"file":("test.csv",csv_content,"text/csv")})
    assert response.status_code == 200 
    data = response.json() 
    assert data["filename"] == "test.csv" 
    assert data["validation"]["valid"] is True 
    assert data["analytics"] is not None
def test_invalid_csv_excel_file():
    csv_content = """random_name1,random_name2,Sales Amount,Product Category,Region,Sale Date
             2,10,20,A,North,2025-01-01 
             3,20,60,B,South,2025-01-02 """
    response=client.post("/upload",files={"file":("test_2.csv",csv_content,"text/csv")})
    assert response.status_code == 200 
    data = response.json() 
    assert data["filename"] == "test_2.csv" 
    assert data["validation"]["valid"] is False
    assert data["analytics"] is None
def test_false_extension_file():
    csv_content = """Quantity Sold,Unit Price,Sales Amount,Product Category,Region,Sale Date
          2,10,20,A,North,2025-01-01 3,20,60,B,South,2025-01-02 """
    response=client.post("/upload",files={"file":("test_3.txt",csv_content,"text")})
    assert response.status_code == 400
    data= response.json() 
    assert "Unsupported file type. Please upload a CSV or Excel file." in data["detail"]
def test_unreadable_right_extension_file():
    csv_content = ""
    response=client.post("/upload",files={"file":("test_4.csv",csv_content,"text")})
    assert response.status_code == 400
    data=response.json()
    assert 'The file could not be read.' in data["detail"]

