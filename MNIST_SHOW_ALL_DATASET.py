# use matlab for complete MNIST DATASET, use .mat file

from scipy.io import loadmat # import เพื่อสามารถดึงข้อมูล .mat มาใช้ได้
import matplotlib.pyplot as plt #for create image
mnist_law = loadmat("mnist-original.mat") # ดึงข้อมูลจาก .mat มาใช้
mnist = { "data":mnist_law["data"].T, "target":mnist_law["label"][0] } # ช่องที่ 0 คือข้อมูลตัวเลข # .T is transpose
x = mnist["data"]   # สร้างตัวแปรไว้เก็บข้อมูล
y = mnist["target"] # บ่งบอกรูปภาพที่แสดงผลว่าเป็นข้อมูลอะไร

number = x[35000]  # เอาไว้ดึงข้อมูลจากตัวแปร x, ดึงตำแหน่งที่ต้องการเพื่อนำมาใช้แสดงผล
number_image = number.reshape(28,28) # Data แสสงผล และทำการแปลงภาพให้เป็น array 2 มิติด้วยคำสั่ง reshape

plt.imshow(number_image, cmap=plt.get_cmap("binary"), interpolation="nearest") # create image for show
print(y[35000]) # เพื่อบ่งบอกว่า ตัวเลขที่ 15000 คือข้อมูลตัวอะไร
plt.show() #show image

print(mnist_law) #properties
print(mnist["data"].shape) #70000 data, 28x28 pixel = 784
print(x.shape)




