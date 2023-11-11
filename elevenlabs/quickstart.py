import os

from elevenlabs import generate, play, set_api_key

api_key = os.getenv('API_KEY_ELEVENLABS')
if api_key is None:
    print("请先配置密钥环境变量")
    exit()

# 配置全局请求密钥
# https://github.com/elevenlabs/elevenlabs-python#-api-key
set_api_key(api_key)

story = """Dear Son, I know you're at a crossroads in life right now, dealing with feelings of anger and 
disappointment because a friend has betrayed you. I hope you can learn from my past experiences to understand my 
views on forgiveness. When I was a young man, I had a close friend named Tom. We spent many unforgettable times 
together, sharing joys, sorrows, and challenges. But then, a small misunderstanding led to a bitter argument. I was 
stubborn, thinking that apologizing would be like begging for his forgiveness. I chose to stand my ground. As time 
passed, I lost my friendship with him. Looking back now, I'm filled with regret. I don't want you to make the same 
mistakes I did, becoming stuck in your own stubbornness. Forgive them not because they'll surely apologize or admit 
their wrongs, but to free yourself. Forgiveness isn't about forgetting what they've done wrong to you; it's about 
letting go of the burdens in your heart, releasing yourself from the shackles of hatred and resentment. That's the 
power of forgiveness. When you accept and forgive the hurts you encounter, you're freeing yourself, making yourself 
stronger. You'll realize that life's hardships and challenges aren't out to destroy you—they're guiding you to become 
a better person. I once heard that life is like a mirror. If you smile at it, it returns a smile. Similarly, 
if you manifest forgiveness and understanding, you reap understanding and forgiveness in return. You've always been a 
son to be proud of, and I believe you'll understand what I'm saying and know how to cope with this setback. Remember, 
my son, no matter what life throws at you, you need to learn to forgive and continue to move forward courageously. 
Forgiveness isn't always easy, but it's the only key that can open the doors of your heart for love to enter. Always 
loving you, Your father"""

audio = generate(
    text=story,
    voice="Bella",
    model="eleven_multilingual_v2"
)

if __name__ == '__main__':
    # 在命令行下执行播放音频
    play(audio)

    # 将音频数据保存为音频文件
    with open('output.wav', 'wb') as f:
        f.write(audio)
