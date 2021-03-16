# Data-Labeler-Project
The concept for this project was to make a data labeler using PyQt5 for my Astronomy class creative project.
The idea came to me as a interaction between the professor and the class for a specific part of the lecture. Since we were
forced to be online during COVID, interactions in class was difficult. He started every lecture started off with the
"Astronomy Picture of the Day". This was an image posted by NASA on their webpage. He would then explain key points of interest of the image
to the class.

My idea was to connect the class. The professor would get the image of the day and label it using the interface. Then the students would get the 
image and the annotations files. They would click on the image and select the correct button to identify the label. It was a different format for quizzes.

In order to use this original version:
1. run python3 admin.py (image name)
2. To label in admin.py
   * Find the upper left corner of the boundary box
   * Right click and select new box
   * Left click bottom right corner of the boundary box
   * Answer the dialog box
   * Repeat until all boxes have been created
   * Right click and select quit
3. run python3 client.py (image name) to see the box

The selection of the boxes, selection of the answer, and grade calculation where not completed with in the class.

The other version (WIP) is a data laber for my ML Portfolio. The data labeler will be for eye colors. It will use most of the fuctionallity from admin.py
however, it will be able to label folders of images and have more quality of life to it functionallity.

# Image Loaded
![Proof of concept](https://github.com/wlhoyt/Data-Labeler-Project/blob/main/Proof1.png)
# Notation For Label
![Proof of concept](https://github.com/wlhoyt/Data-Labeler-Project/blob/main/Proof2.png)
# Result From Notation
![Proof of concept](https://github.com/wlhoyt/Data-Labeler-Project/blob/main/Proof3.png)
# Shown In Student GUI
![Proof of concept](https://github.com/wlhoyt/Data-Labeler-Project/blob/main/Proof4.png)

# TODO for repo
- [x] Add current project to the Git Repo for illustration
- [x] Embedded the images into the README

## TODO for stand-alone version
- [ ] Allow for selection of folder locations for images and labels
- [ ] Create a way to cycle labels and images within the GUI
- [ ] Create an undo button
- [ ] Fix edge cases for user error or GUI interactions
