# NIRF-University-Analysis

University Score Prediction and Recommendation based on NIRF (Ministry of Education)

### Objective

Trying to predict the score of universities based on certain parameters set by NIRF which are

- Teaching Learning & Resources - These parameters are related to the core activities of any place of learning.
- Research and Professional Practice - Excellence in teaching and learning is closely associated with the scholarship.
- Graduation Outcome - This parameter forms the ultimate test of the effectiveness of the core teaching/learning.
- Outreach & Inclusivity - The Ranking framework lays special emphasis on representation of women.
- Perception - The ranking methodology gives a significant importance to the perception of the institution.

University recommendation based on the scores obtained by the universities.

### Introduction

In this project, the application gathers and prepares the universities data from the NIRF website(of the desired year). Then feed the prepared data to the model so that it can learn. After then, feed the fresh data (University data) into the trained model and see if the model just trained predict it accurately or not. This application also recommend the university based on the the overall score and the scores under various parameters obtained by the universities.

## Training, Prediction and Recommendation

### Training Data 
Our training data consists of the totals obtained by Universities under various parameters (TLR, RPC, GO, OI, PERCEPTION and Score). All training data can be retrieved from the file NIRF_University2022.csv.

### Prepare Training Data 
Model accepts the scores obtained by universities under the parameters as a input and labels so that for each evaluation the model knows which class the university belongs to and the overall score of the university (originally evaluated by NIRF).

### For example:

(For Score Prediction)

Features

- TLR(100) - 82.08
- RPC(100) - 87.45
- GO(100) - 84.80
- OI(100) - 57.46
- PERCEPTION(100) - 100.00

Labels

Score - 83.57
(For Recommendation)

Features

- TLR(100) - 82.08
- RPC(100) - 87.45
- GO(100) - 84.80
- OI(100) - 57.46
- PERCEPTION(100) - 100.00
- Score - 83.57

Labels

Recommend - 1


## Software Requirements

### Languages and Packages used

● Python3.6+ , Libraries - pandas, sklearn, bs4, matplotlib

● Platform - Google Colab

### Hardware Requirements

● System Processor: i3 or later.

● RAM: 4GB DDR RAM.(Minimum)
