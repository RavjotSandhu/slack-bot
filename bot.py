
import os
from slack import WebClient
from slack.errors import SlackApiError
import GetOldTweets3 as got

if __name__ == "__main__":
 slack_token = os.environ["SLACK_BOT_TOKEN"]
 client = WebClient(token=slack_token)

 tweetCriteria = got.manager.TweetCriteria().setUsername("elonmusk")\
                                           .setMaxTweets(10)
 tweet = got.manager.TweetManager.getTweets(tweetCriteria)[0]

 try:
  response = client.chat_postMessage(
    channel="#random",
    text=tweet.text
   )
 except SlackApiError as e:
  assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
