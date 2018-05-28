#generates stories for a folfer of images --useful when evaluating
#sj2842
import glob
import generate
z = generate.load_all()
# from IPython.core.display import Image, display
# from PIL import Image as Img
for filename in glob.iglob('/Users/shreyajain/storyteller/neural-storyteller/images2/*'):
    print('%s' % filename)
    # display(Image(filename))
    generate.story(z, filename)
    print("########## Parameters set k = 200 and bw=50 ###############")
    print(generate.story(z, filename,k=200, bw=50))
    # print("########## Parameters set k = 300 and bw=100 ###############")
    # print(generate.story(z, filename, k=300, bw=50))
    # print("########## Parameters set k = 400 and bw=100 ###############")
    # print(generate.story(z, filename, k=400, bw=50))
	

