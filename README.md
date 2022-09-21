# Live Sentiment Analysis from Twitter
## Live Sentiment Analysis on COVID-19 tweets from Twitter
#### By Arunava Kumar Chakraborty

In this experimental approach, I have developed a simple Sentiment Analysis Application that will perform the following operations
1. First the application is fetching the tweets on **"COVID-19"** from Twitter I have used the **tweepy** API for **python** to do so. I have created a Twitter developer account for creating an application to generate the Twitter credentials for the app These are - **consumer key**, **consumer secret key**, **access token key**, **access secret key**.
2. The fetched tweets are cleaned and preprocessed by using the **NLTK (Natural Language Toolkit)** package thus the stop words can be removed.
3. The cleaned and pre-processed tweets are stored in an **SQLite Database File** (.db format).
4. The Sentiment ratings for each tweet are calculated using the **vaderSentiment** package in **python** and stored those values in the database.
5. Finally, after calculating the sentiment of the tweets the Sentiment Polarities are visualized through graphs using the **plotly**, **dash** packages in python.

### Required Packages
Please install the following packages to execute all the codes.

- **tweepy**==4.4.0
- **pandas**==1.3.4
- **plotly**==5.9.0
- **dash**==2.0.0
- **preprocessor**==1.0.2
- **nltk**==3.6.5
- **vaderSentiment**==3.3.2
- **unidecode**==1.2.0
