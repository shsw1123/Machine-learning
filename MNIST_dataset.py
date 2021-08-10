# ชุดข้อมูลตัวเลขอราบิก 0-9 มีขนาดรูป 28x28 pixel ชุดเรียนรู้จำนวน 60,000 รูปภาพและข้อมูลชุดทดสอบจำนวน 10,000 รูปภาพ,
# Training set = ให้เครื่องจักรเรียนรู้ สร้าง model, Test set = ทดสอบโมเดลว่าประสิทธิภาพดีพอจะไปใช้จริงไหม
# scikit learn มีข้อมูลน้อยกว่า 8x8 pixel ไม่งั้นต้องใช้ matlab ในการ import
from sklearn import datasets
digit_dataset = datasets.load_digits()

print(digit_dataset.keys())
#print(digit_dataset['data'])
#print(digit_dataset['data'][0:10])
#print(digit_dataset['target'])
#print(digit_dataset['feature_names'])
#print(digit_dataset['target_names'])
#print(digit_dataset['DESCR'])
#print(digit_dataset['images'].shape) # มีกี่ข้อมูล และขนาดกี่ pixel
#print(digit_dataset.data)
#print(digit_dataset.images.shape) # ได้เช่นกัน
print(digit_dataset.images[0:10]) # ข้อมูลขอตัวแรก
