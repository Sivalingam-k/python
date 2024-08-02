class Brand:
    # product_name=input("Enter Product Name :")
    def __init__(self,brand_name):
        self._brand_name = brand_name
    def displayBrand_name(self):
        print("Brand Name: ", self._brand_name )
    
class Product:
    _product_id=0
    def __init__(self):
        self.product_name=input("Enter Product Name :")
        self.product_price=input("Enter Product Price :")
        self.product_description=input("Enter Product Description :")
        Product._product_id+=1
        self.product_id=self._product_id
        
    def getprodetails(self):
        print("Product ID : ",self.product_id)
        print("Product Name: ", self.product_name)
        print("Product Price: ",self.product_price)
        print("product Description : ",self.product_description)


b1 = Brand("Redux")
b1.displayBrand_name()

print()
p1=Product()
p1.getprodetails()
print("Product Added Successfully!!")
p2=Product()
p2.getprodetails()
print("Product Added Successfully!!")








