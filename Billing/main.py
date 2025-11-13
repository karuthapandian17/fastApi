from fastapi import FastAPI , Body , Depends
from app.database import databaseConfigration
from app.database.models.userModel import ProductModel, invoiceModel, invoiceItemModel
from fastapi.exceptions import HTTPException

app = FastAPI()

databaseConfigration.create_database()

def get_db():
    connection = databaseConfigration.create_database()
    if connection is None:
        raise HTTPException(status_code=500, detail="mysql connection error")
    try:
        yield connection
    finally:
        if connection and connection.is_connected():
            print("connected sucessfully")    

@app.get("/")
def home():
    return "Hello First Project"

@app.post("/createProduct", response_model=dict)
async def add_product(product:ProductModel = Body(...), connection = Depends(get_db)):
   
    try:
            cursor = connection.cursor()
            insert_query ="INSERT INTO product (id, name, price, gst_percent, stock, sku) VALUES (%s,%s,%s,%s,%s,%s)"
            cursor.execute(insert_query, (product.id, product.name, product.price, product.gst_percent, product.stock, product.sku))
            connection.commit()
            print("Product created.......")
            databaseConfigration.ConnectionClose(connection)
            return{"message": 'Product created'}
    except Exception as  e:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    
@app.get('/get', response_model=dict)
async def get_product(connection=Depends(get_db)):
    try:
            cursor = connection.cursor()
            insert_query = "SELECT * FROM `product`"
            cursor.execute(insert_query)
            data = cursor.fetchall()
            connection.commit()
            if not data:
                 return {"message":"no product"}

            databaseConfigration.ConnectionClose(connection)
            return{"message": data}
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Database error:{str(e)}")

@app.post('/update', response_model=dict)
async def update_product(product:ProductModel = Body(...), connection=Depends(get_db)):
    try:
            cursor = connection.cursor()
            insert_query = "UPDATE product SET name =%s , price =%s , gst_percent =%s, stock=%s,  sku=%s WHERE id =%s"
            cursor.execute(insert_query, ( product.name , product.price, product.gst_percent, product.stock, product.sku,product.id,))
            
            connection.commit()
           

            databaseConfigration.ConnectionClose(connection)
            return{"message": "updated sucessfully"}
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Database error:{str(e)}")

@app.delete('/delete', response_model=dict)
async def delete_product(product: ProductModel = Body(...), connection=Depends(get_db)):
    try:
            cursor = connection.cursor()
            insert_query = "DELETE FROM product WHERE id =%s "
            cursor.execute(insert_query, (product.id,))
            
            connection.commit()
           

            databaseConfigration.ConnectionClose(connection)
            return{"message": "deleted sucessfully"}
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Database error:{str(e)}")            
    
@app.post("/createInvoices", response_model=dict)
async def add_invoice(invoice:invoiceModel = Body(...), connection = Depends(get_db)):
   
    try:
            cursor = connection.cursor()
            insert_query ="INSERT INTO invoices (id, invoice_number, date , customer_name, phone, total_amount, gst_amount, grand_total ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(insert_query, (invoice.id, invoice.invoice_number, invoice.date, invoice.customer_name, invoice.phone, invoice.total_amount, invoice.gst_amount, invoice.grand_total))
            connection.commit()
            print("invoice created.......")
            databaseConfigration.ConnectionClose(connection)
            return{"message": 'invoice created'}
    except Exception as  e:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    
@app.get('/getInvoices', response_model=dict)
async def get_invoice(connection=Depends(get_db)):
    try:
            cursor = connection.cursor()
            insert_query = "SELECT * FROM `invoices`"
            cursor.execute(insert_query)
            data = cursor.fetchall()
            connection.commit()
            if not data:
                 return {"message":"no invoices"}

            databaseConfigration.ConnectionClose(connection)
            return{"message": data}
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Database error:{str(e)}")

@app.post('/updateInvoices', response_model=dict)
async def update_invoice(invoice:invoiceModel = Body(...), connection=Depends(get_db)):
    try:
            cursor = connection.cursor()
            insert_query = "UPDATE invoices SET invoiceNumber =%s , date =%s , customerName =%s, phone=%s,  total_amount=%s, gst_amount=%s, grand_total=%s WHERE id =%s"
            cursor.execute(insert_query, (invoice.invoice_number, invoice.date, invoice.customer_name,invoice.phone, invoice.total_amount,invoice.gst_amount,invoice.grand_total,invoice.id,))
            
            connection.commit()
           

            databaseConfigration.ConnectionClose(connection)
            return{"message": "updated sucessfully"}
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Database error:{str(e)}")

@app.delete('/deleteInvoices', response_model=dict)
async def delete_invoice(invoice:invoiceModel = Body(...), connection=Depends(get_db)):
    try:
            cursor = connection.cursor()
            insert_query = "DELETE FROM invoices WHERE id =%s "
            cursor.execute(insert_query, (invoice.id,))
            
            connection.commit()
           

            databaseConfigration.ConnectionClose(connection)
            return{"message": "deleted sucessfully"}
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Database error:{str(e)}")

@app.post("/createInvoiceItems", response_model=dict)
async def add_invoiceItem(invoiceItem:invoiceItemModel = Body(...), connection = Depends(get_db)):
   
    try:
            cursor = connection.cursor()
            insert_query ="INSERT INTO invoice_items (id, invoice_id , product_id , quantity, price, gst_percent, total ) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(insert_query, (invoiceItem.id, invoiceItem.invoice_id, invoiceItem.product_id, invoiceItem.quantity, invoiceItem.price, invoiceItem.gst_persent, invoiceItem.total))
            connection.commit()
            print("invoice_items created.......")
            databaseConfigration.ConnectionClose(connection)
            return{"message": 'invoice_items created'}
    except Exception as  e:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

@app.get('/getInvoicesItems', response_model=dict)
async def get_invoiceItem(connection=Depends(get_db)):
    try:
            cursor = connection.cursor()
            insert_query = "SELECT * FROM `invoice_items`"
            cursor.execute(insert_query)
            data = cursor.fetchall()
            connection.commit()
            if not data:
                 return {"message":"no invoice_items"}

            databaseConfigration.ConnectionClose(connection)
            return{"message": data}
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Database error:{str(e)}")

@app.post('/updateInvoicesItem', response_model=dict)
async def update_invoiceItem(invoiceItem:invoiceItemModel = Body(...), connection=Depends(get_db)):
    try:
            cursor = connection.cursor()
            insert_query = "UPDATE invoice_items SET invoice_id =%s , product_id =%s , quantity =%s, price=%s,  gst_percent=%s, total=%s WHERE id =%s"
            cursor.execute(insert_query, (invoiceItem.invoice_id, invoiceItem.product_id, invoiceItem.quantity, invoiceItem.price, invoiceItem.gst_persent, invoiceItem.total,invoiceItem.id,))
            
            connection.commit()
           

            databaseConfigration.ConnectionClose(connection)
            return{"message": "updated sucessfully"}
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Database error:{str(e)}")

@app.delete('/deleteInvoicesItem', response_model=dict)
async def delete_invoiceItem(invoiceItem:invoiceItemModel = Body(...), connection=Depends(get_db)):
    try:
            cursor = connection.cursor()
            insert_query = "DELETE FROM invoice_items WHERE id =%s "
            cursor.execute(insert_query, (invoiceItem.id,))
            
            connection.commit()
           

            databaseConfigration.ConnectionClose(connection)
            return{"message": "deleted sucessfully"}
    except Exception as e:
        connection.rollback()
        raise HTTPException(status_code=500, detail=f"Database error:{str(e)}")                            
        