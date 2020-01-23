import matplotlib.pyplot as plt 
import cv2
import sys

def Main():
	if len(sys.argv) < 2:
		print('Must supply an image.')
		sys.exit(1)
	img = cv2.imread(sys.argv[1])
	
	# opencv reads RGB images as BGR so we  convert them
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

	# Space for an RGB histogram
	reds = [ 0 ] * 256
	grns = [ 0 ] * 256
	blus = [ 0 ] * 256
	# Consecutive numbers to serve as x axis for histogram
	xs = list(range(256))

	red_img = img.copy()
	grn_img = img.copy()
	blu_img = img.copy()
	gry_img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
	# The _ next line means "don't care about the returned value"
	height, width, _ = img.shape

	print('Processing...')
	for y in range(height):
		for x in range(width):
			# Seperate channels
			red_img[y, x] = (img[y, x][0], img[y, x][0], img[y, x][0])
			grn_img[y, x] = (img[y, x][1], img[y, x][1], img[y, x][1])
			blu_img[y, x] = (img[y, x][2], img[y, x][2], img[y, x][2])
			# Build channel histogram
			reds[img[y, x][0]] += 1
			grns[img[y, x][1]] += 1
			blus[img[y, x][2]] += 1

	figure, axs = plt.subplots(nrows= 3, ncols=2)
	(ax1, ax2), (ax3, ax4), (ax5, ax6) = axs

	figure.suptitle('RGB Image and its Channels')
	
	ax1.set_title('RGB')
	ax1.imshow(img)
	
	ax2.set_title('GRAY')
	ax2.imshow(gry_img, cmap=plt.cm.gray)
	
	ax3.set_title('RED')
	ax3.imshow(red_img)
	
	ax4.set_title('GREEN')
	ax4.imshow(grn_img)
	
	ax5.set_title('BLUE')
	ax5.imshow(blu_img)
	
	ax6.plot(xs, reds, 'r')
	ax6.plot(xs, grns, 'g')
	ax6.plot(xs, blus, 'b')
	
	plt.show()

if __name__ == '__main__':
	Main()