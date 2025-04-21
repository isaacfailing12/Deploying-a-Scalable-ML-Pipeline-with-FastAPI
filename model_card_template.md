# Model Card - Salary Prediction

## Model Details
This model is made to predict if a person’s income is more than $50,000 a year. It uses information like their education, job type, relationship status, race, gender, and where they are from. The model is built using a Random Forest Classifier, and the data was cleaned and prepared before training.

## Intended Use
The model is meant to be used inside a web service (API) where someone can send in a person's details and get back a prediction about their income level. It should be used for research, learning, or helping applications make better guesses — not for important decisions about real people without checking carefully.

## Training Data
The model was trained on the "census.csv" file. This file has lots of people’s information, like their jobs, education, and other background details. We cleaned the data by turning text into numbers so the model could understand it.

## Evaluation Data
80% of the data was taken to train the model and kept 20% to test how well it works. I made sure to process the test data the same way the training data was processed.

## Metrics
Checked how good the model is by looking at three scores:

- Precision: 0.7419

- Recall: 0.6384

- F1 Score: 0.6863

Also checked how the model works for different groups, like different races, genders, or education levels, to see if it works better for some groups than others.

## Ethical Considerations
The model was trained with real-world data, so it might pick up unfair patterns (like treating some groups better or worse). Who decides to use this should be careful using this model for important things like hiring or loans.

## Caveats and Recommendations
The model doesn't always perform the same for every group of people. Sometimes it works better for some groups than others. If you use the model for a long time, it’s a good idea to keep checking and updating it. Also, it’s best used for people living in the U.S., since that's what the training data is based on.