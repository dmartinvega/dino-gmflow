import torch



import torchvision
import matplotlib.pyplot as plt

image = torchvision.io.read_image("woman-and-dog.jpg")
image = torchvision.transforms.Resize((14*5, 14*5), torchvision.transforms.InterpolationMode.NEAREST)(image)

plt.imshow(image.permute(1,2,0))
plt.show()


image = torch.unsqueeze(image, 0)
image = torchvision.transforms.functional.convert_image_dtype(image, torch.float)
image = image.cuda()

dinov2_vits14 = torch.hub.load('facebookresearch/dinov2', 'dinov2_vits14')
dinov2_vits14.eval()
dinov2_vits14.cuda()

result = dinov2_vits14.forward(image)

result = result.squeeze(0)
result = result.resize([14*5, 14*5])
plt.imshow(result.permute(1,2,0).cpu().detach().numpy())
plt.show()
show(result)
print('dinov2_vits14 loaded')

