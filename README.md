# Image-Classifier

In everyday life, we may need to separate the men from the boys, the wheat from the chaff, or the sheep from the goats. Hence, in this assessment, you will build an image classifier for images of your choosing. Don't use cats/dogs; use something else - you choose. But only use two or three classes.

###I have made available a program called download_images.py on Canvas. Use it to create your dataset.
-To install:
-Remember to activate your virtual environment first.
-Then install an extra library as follows:
-$ pip install git+https://github.com/Joeclinton1/google-images-download.git
-To run, type (e.g.):
-$ python3 download_images.py 100 cat dog
-You won't be allowed a number bigger than 100. And some images may fail to download, so you may end up with fewer than 100.
-It places the images into a folder called downloads.
-Clean your dataset.
-Some ideas for doing this:

-On a Mac, make sure you don't have any of those stupid .DS files or __MACOS folders.
-Manually delete any of the downloaded images that are not JPEGs.
-Scan through the images manually and delete any that you think are not great examples, i.e. in this case, delete images that aren't good examples of cats or dogs.
-Corrupted exif values may cause problems during training. Clean them using ExifTool by Phil Harvey.
-To install:
-Download it from https://github.com/exiftool/exiftool
-Unzip it.
-To run it:

-Type:
-$ ./exiftool-master/exiftool -r -all= -ext JPG ./downloads
-Look at the messages it spews out. If it complains about any of the images, then manually delete those images from your dataset.
-ExifTool saves copies of the original images. Delete them by typing:
-$ find ./downloads -type f -name '*jpg_original*' -delete
-Supplement your dataset: manually download a few extra images to compensate for the ones that didn't download and the ones that you deleted. When you finish you should have 100 images of each class.
-I have made available a program called partition_images.py on Canvas. Use it to split your dataset into three.
-To install:

-Remember to activate your virtual environment first.
-Then install an extra library as follows:
-$ pip install split-folders
-To run, type (e.g.):

-$ python3 partition_images.py downloads 0.5 0.25
-In this CA, I recommend a 50%-25%-25% split, as above.

-It creates three new folders: train, val and test.

-Afterwards, when you're sure you're done, delete the downloads folder (or move it somewhere).

-Create a Jupyter notebook called ai2_training.ipynb. In this Jupyter notebook, use transfer learning to build one or more neural network classifiers for your dataset. Your different classifiers may differ in their architectures (i.e. their layers), their learning rates, their use of data augmentation, and so on. (Of course, it is better if one classifier is motivated by failings of the previous one, e.g. if the previous one overfits, then the next one can try to remedy the overfitting.) Make sure your notebook includes markdown cells to explain what you are doing/why you are doing it/how you are doing it/etc. In the grading, this is just as important as the code.
-The final cell of your notebook should save your best classifier to a file. If your best model is called best_network, for example, then the last cell of your notebook will contain the following:

-best_network.save("best_network.h5")
-Create a folder called examples. Into this folder, place up to 6 images. They might be copies of test set images; or they might be new images that you've downloaded from the web or that you've taken yourself; or a mixture. Either way, they should be carefully selected for use in step 7.
-Create a Jupyter notebook called ai2_demo.ipynb. In this Jupyter notebook, use the images that you selected in step 6 to highlight some strengths and weaknesses of the classifier that you saved in step 5. Again use markdown cells to give me some narrative: why do you think it gets things right/why do you think it gets things wrong/etc.
-Obviously one of the earliest cells of this notebook will need to load the classifier:

-best_network = load_model("best_network.h5")
-And another will need to load the images from the examples folder, e.g.:

-path = "examples"
-pathnames = [os.path.join(path, filename) for filename in sorted(os.listdir(path))]

-imgs = [load_img(img_path, target_size=(224, 224)) for img_path in pathnames]
-for img in imgs:
 -   plt.figure()
  -  plt.imshow(img)
-On completion, you should have a folder that contains the following files:
-ai2_training.ipynb
-ai2_demo.ipynb
-best_network.h5
-and the following folders:

-train
-val
-test
-examples
