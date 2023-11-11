# coding=utf-8
import os

# 快速开始：https://help.aliyun.com/zh/dashscope/developer-reference/quick-start-13
# 安装DashScope SDK：https://help.aliyun.com/zh/dashscope/developer-reference/install-dashscope-sdk

import dashscope
from dashscope.audio.tts import SpeechSynthesizer

dashscope.api_key = os.getenv('API_KEY_ALIYUN_DASHSCOPE')

story = """亲爱的儿子，
我知道你现在正处在生活的十字路口，你的朋友背叛了你，你的心里充满了愤怒和失望。我希望你能从我的过去中学些东西，理解我对宽恕的看法。
当我还是个年轻人的时候，我有个朋友，名叫汤姆。我们一起度过了许多难忘的时光，一起分享了许多悲喜和困难。有一次，因为一个小小的误会，我们吵了起来。我太固执，以为去道歉就是在乞求他的原谅，于是我选择坚持自己的立场。时间过去，我失去了他这个朋友，现在想来，我的心中充满了遗憾。
我不希望你犯我当年的错误，被自己的执拗困住。原谅他们，不是因为他们一定会道歉，或者他们认识到自己的过错，而是让你自己得到释放。原谅他人不是忘记他们对你做过的坏事，而是放下心中的负担，让自己的人生不再被憎恨和怨恨束缚。这就是宽恕的力量。
当你接受并原谅你所遇到的伤害，你就在释放自己，让自己的心灵变得更强大。你会发现，生活中的困难和挑战，并不是在试图毁掉你，而是在引导你，让你成为更好的人。
我曾听人说过，生活是一面镜子，如果你对着它笑，它就会回报给你一个笑容。同样，如果你能带着宽恕和理解去面对别人，你同样会收获他人的理解和宽恕。
你一直是我无比自豪的儿子，我相信你会理解我的意思，并且懂得如何处理这次的挫折。
记住，儿子，无论生活怎么对你，你都要学会宽恕，坚强地前进。宽恕并不总是易事，但它是唯一能打开你的心门，让爱流进来的钥匙。
永远爱你的，父亲"""

story_english = """Dear Son,
I know you're at a crossroads in life right now, dealing with feelings of anger and disappointment because a friend has betrayed you. I hope you can learn from my past experiences to understand my views on forgiveness.
When I was a young man, I had a close friend named Tom. We spent many unforgettable times together, sharing joys, sorrows, and challenges. But then, a small misunderstanding led to a bitter argument. I was stubborn, thinking that apologizing would be like begging for his forgiveness. I chose to stand my ground. As time passed, I lost my friendship with him. Looking back now, I'm filled with regret.
I don't want you to make the same mistakes I did, becoming stuck in your own stubbornness. Forgive them not because they'll surely apologize or admit their wrongs, but to free yourself. Forgiveness isn't about forgetting what they've done wrong to you; it's about letting go of the burdens in your heart, releasing yourself from the shackles of hatred and resentment. That's the power of forgiveness.
When you accept and forgive the hurts you encounter, you're freeing yourself, making yourself stronger. You'll realize that life's hardships and challenges aren't out to destroy you—they're guiding you to become a better person.
I once heard that life is like a mirror. If you smile at it, it returns a smile. Similarly, if you manifest forgiveness and understanding, you reap understanding and forgiveness in return.
You've always been a son to be proud of, and I believe you'll understand what I'm saying and know how to cope with this setback.
Remember, my son, no matter what life throws at you, you need to learn to forgive and continue to move forward courageously. Forgiveness isn't always easy, but it's the only key that can open the doors of your heart for love to enter.
Always loving you, Your father"""

if __name__ == '__main__':
    # 使用指定模型将文本转语音
    result = SpeechSynthesizer.call(model='sambert-zhiyuan-v1', text=story_english)

    # 输出音频文件
    if result.get_audio_data() is not None:
        with open('output.wav', 'wb') as f:
            f.write(result.get_audio_data())
