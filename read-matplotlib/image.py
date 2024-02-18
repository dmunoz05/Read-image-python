import matplotlib.pyplot as plt

img = plt.imread('girasol.jpg')
# plt.figure(figsize=(10, 5))
# plt.subplot(2, 3, 1)
plt.imshow(img)
plt.axis("off")
plt.show()