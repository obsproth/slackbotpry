"""Main Module
Slack RTM APIのイベント処理により動作するbotを起動する
"""
import sys
import argparse
from slackclient import SlackClient

def make_argparser():
    """Create Command Line Parser
    DESCRIPTION:
        This function creates ArgumentParser Object and make arguments for this app.
    NOTE:
        今後の拡張性のためにArgumentParserオブジェクトでコマンドラインのパースをしていますが今のところ
        python slackbotpry APITOKEN
        ってだけです
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("--channel", "-c", default="random", help='channel to post message')
    parser.add_argument("APITOKEN", type=str, help='api token for slack bot/integration you use')
    return parser
def get_channel(slack: SlackClient, channel_name: str):
    """get the channel_name for integration
    NOTE:一応DMや自分DM等の対応のための余地として作っといた
    """
    return channel_name
def main():
    """Main Routine
    PROCESS:
        1.analyze commandline
        2.get api_token
        3.post to slack
    """
    import bot
    # parse commandline arguments
    argparser = make_argparser()
    argument = argparser.parse_args()
    # get api token
    api_token = argument.APITOKEN
    slack = SlackClient(token=api_token)
    mybot = bot.Bot(slack, argument.channel)
    from eventhandler import SimpleMessageHandler
    callback = lambda bot, text : bot.post_message('Hi')
    mybot.add_eventhandler(SimpleMessageHandler(r'^Hello$', callback))
    mybot.mainloop()
if __name__ == "__main__":
    main()