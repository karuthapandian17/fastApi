
from pydantic import BaseModel

class ProductModel(BaseModel):
    id:int
    name:str
    price:int
    gst_percent:int
    stock:int
    sku:str

class invoiceModel(BaseModel):
    id:int
    invoice_number:str
    date:int
    customer_name : str
    phone : int
    total_amount :int
    gst_amount:int
    grand_total:int    

class invoiceItemModel(BaseModel):
    id:int 
    invoice_id : int
    product_id : int
    quantity : int
    price : int
    gst_persent : int
    total : int   