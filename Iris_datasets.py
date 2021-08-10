from sklearn import datasets #import
# สายพันธ์ดอกไม้

iris_dataset = datasets.load_iris() # load data set iris

print(iris_dataset.keys()) # ดู key dataset, DESCR เก็บข้อมูลรายละเอียดไว้
print(iris_dataset['target']) # เก็บข้อมูลสายพันธ์ของดอกไม้ เป็ฯตัวเลข
print(iris_dataset['target_names']) # ชื่อของข้อมูล target ที่เก็บไว้เป็นตัวเลข
print(iris_dataset['DESCR']) # เพื่อบ่งบอกว่า iris dataset เก็บเกี่ยวกับอะไร โดยจะเก็บความกว้าง ความยาวของกรีบเลี้ยง กรีบดอก และอื่นๆ
print(iris_dataset['feature_names']) # บ่งบอกคุณสมบัติของ Dataset เก็บข้อมูลอะไรบ้าง
print(iris_dataset['data']) # ข้อมูลที่เก็บไว้ของ dataset
print(iris_dataset['data'][0:10]) # ระบุขอบเขตของข้อมูล 10 แถวแรก