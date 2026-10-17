# AI Image Analysis: Emotion & Object Detection with Amazon Rekognition

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Boto3](https://img.shields.io/badge/Boto3_(AWS_SDK)-232F3E?style=flat-square)
![Amazon Rekognition](https://img.shields.io/badge/Amazon_Rekognition-FF9900?style=flat-square)
![Pillow](https://img.shields.io/badge/Pillow-3776AB?style=flat-square)
![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C?style=flat-square)

A computer vision pipeline that takes a busy street scene and returns what's in it: every face with its predicted expression, every object with a label, and confidence scores drawn right onto the image.

📄 **Full case study:** [AI Image Analysis: Emotion & Object Detection](https://iamnicolecoleman.com/portfolio/case-study-ai-powered-image-analysis-for-emotion-and-object-detection/)

<p align="center">
  <img src="https://iamnicolecoleman.com/wp-content/uploads/2025/01/Screenshot-2024-12-14-at-12.08.30%E2%80%AFAM.png" width="100%" alt="Annotated output with bounding boxes and confidence scores"/>
</p>

## Skills demonstrated

| Skill | Where it shows up |
|---|---|
| Cloud AI services | Amazon Rekognition face analysis and label detection APIs |
| API integration | Python and Boto3 to send images and parse the JSON responses |
| Computer vision output handling | Converting Rekognition's relative bounding boxes into pixel coordinates |
| Visualization | Drawing boxes, labels, and confidence scores with Pillow and Matplotlib |
| Solution framing | Mapping the output to use cases like retail analytics, event engagement, and crowd management |

## How it works

```mermaid
flowchart LR
    A[Street scene image] --> B[Python + Boto3]
    B --> C[Rekognition<br/>DetectFaces]
    B --> D[Rekognition<br/>DetectLabels]
    C --> E[Expression labels<br/>+ confidence]
    D --> F[Objects<br/>+ confidence]
    E --> G[Pillow / Matplotlib<br/>annotated image]
    F --> G
```

1. **Faces:** Rekognition's facial analysis returns each face's location and predicted expressions (such as happy, surprised, or angry) with a confidence score.
2. **Objects:** label detection finds people, handbags, clothing, and other objects in crowded, fast-moving scenes.
3. **Visualization:** the script draws bounding boxes and labels on the original image so the results are readable at a glance, not buried in JSON.

## Where this applies

- **Retail:** what shoppers carry and how they move through a space
- **Events:** engagement and crowd density
- **Operations:** turning large batches of images into structured, searchable data

> Note: expression labels describe how a face looks, not how a person actually feels. They're a signal to review, not a conclusion.

## What I learned

- Clear visualization is what makes AI output usable for non-technical people
- Managed cloud AI services let a small team ship computer vision without training a model
- The value is in pairing the technical output with a specific business question

---

**Nicole Coleman** · AWS Community Builder (AI Engineering) · [LinkedIn](https://www.linkedin.com/in/nicoledcoleman/) · [Portfolio](https://iamnicolecoleman.com)
