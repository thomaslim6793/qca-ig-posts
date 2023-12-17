# API Research for Quantitative Content Analysis of Instagram Posts

## Task Description:
I would like to conduct a quantitative content analysis of Instagram posts using AI/ML techniques. So far, researchers have created a codebook and hired labelers to detect various features in the images manually. I'm interested in exploring comparable pre-existing AI methods that can detect these features as good as humans do and reduce the time required for analysis. The objective is to find Github pages, related papers, and API services that can assist in identifying stylistic and compositional features of images for critical visual discourse analysis.

Below are the desired features and some resources:

1. Camera angle: high angle/regular angle/low angle
   - https://github.com/pidahbus/deep-image-orientation-angle-detection
      - source paper: https://arxiv.org/abs/2007.06709

2. Presence of government/police/law enforcement (or occupation detection):
   - a. The number of uniformed police/law enforcement/security personnel shown
   - b. No police
   
3. Number of people:
   - a. Individuals: 1-3 identifiable human subjects shown
   - b. Group: 2-9 identifiable human subjects shown in focus
   - c. Crowd: 10+ identifiable human subjects shown in focus
   - https://github.com/pjreddie/darknet
      - source paper: https://arxiv.org/pdf/1506.02640.pdf
      - Model name: YOLO
      - Annotation method: bounding box annotation
      - use case: https://opencv-tutorial.readthedocs.io/en/latest/yolo/yolo.html
      - Main developer of YOLO:  Joseph Redmon

4. Presence of eye contact:
   - https://github.com/vita-epfl/looking
      - source paper: https://arxiv.org/abs/2112.04212
      - Model architecture itself it derivative of others, e.g. can use alexnet or resnet etc as 
      base model
      - Annotation method: keypoint annotation 
         - Each detected object is annotated with its key points, resulting in a "stick figure"
         like representation of each object rather than a box. 
      - Authors created and a domain specific dataset: LOOK
      - Also uses publically available dataset: JAAD, and PIE     

5. Gender:
   - a. Female
   - b. Male
   - c. Mix of male and female
   - d. Indeterminate (face is not shown)
   - Resources:
      - paper: https://arxiv.org/abs/2004.10934
      - code: https://github.com/AlexeyAB/darknet#how-to-train-to-detect-your-custom-objects
      - Model: YOLO with custom object detection

6. Age:
   - a. Child: <18 years of age
   - b. Young adult: 18-34 years of age
   - c. Mid adult: 35-50 years of age
   - d. Mix
   - e. Indeterminate
   - Resources:
      - https://github.com/mowshon/age-and-gender (object detection: age, gender)

7. Distance (camera shot type):
   - a. Closeup: face and shoulders
   - b. Mid-range: waist up or occupying almost full frame
   - c. Long-range: person's fill half the picture frame or less
   - Resources:
      - https://rsomani95.github.io/ai-film-1.html
         - Project is no longer open source, now need permission from creator to use it...
      - https://anyirao.com/projects/ShotType.html
         - This project doesn't provide a model to use, but does provide a dataset of 
           short video clips and a corresponding annotation file in JSON format. 
8. Facial expression:
   - Smile/anger/disappointed/...
   - Resources:
      - https://github.com/richmondu/libfaceid (object classification (unclear of detection performance): facial expression, age, gender)
      - https://github.com/juan-csv/Face_info (object detection: emotion, race, gender, age)

9. Race or skin color or ethnicity:
   - a. White
   - b. Black
   - c. Asian
   - Resources:
      - https://github.com/wondonghyeon/face-classification (object detection: race, gender)

10. Object detection: Further research is needed to find specific resources for this feature.
   Resources:
      - General purpose object recognition:
         - Amazon Rekognition: https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/what-is.html
            - Uses AWS API and streamlined web-browser console to create custom models for object detection tasks.
            - Use Cases: Basically any object recognition task, at the expense of manually labeling and preparing
            training dataset.
         - OpenCV: https://opencv.org/
            - One of the most popular libraries for computer vision tasks. A rich library with tools allowing people to
            develop your own ml algorithms, or use pre-trained models.  
            - Use cases: Detecting number of people - OpenCV YOLO algorithm: https://opencv-tutorial.readthedocs.io/en/latest/yolo/yolo.html

11. The size of the object/subject: Further research is needed to find specific resources for this feature.

12. Color contrast/diversity: Further research is needed to find specific resources for this feature.
   - Resources: For this task, perform color analysis of images and produce statistics and measures of color contrast or diversity.
      - OpenCV: A comprehensive library for computer vision tasks, it offers functions to compute color histograms, clustering, and more.
      - Scikit-image: Another Python library focused on image processing. It can be used to compute image statistics, like entropy.
      - ColorThief: A Python library that extracts color palettes from images. It can be used as a starting point to understand color distribution.


Please note that while some features have existing Github pages or papers, others require additional exploration. The github pages I refer to should also be checked whether we can use their sources for our own purposes. I recommend reviewing the mentioned sources and continuing the search for additional resources to ensure a comprehensive analysis of all desired visual features for critical visual discourse analysis.

