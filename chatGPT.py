from openai import OpenAI
from config import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

messages = [
    {
      "role": "system",
      "content": [
        {
          "type": "text",
          "text": "1. Repeat the given Japanese word or sentence with furigana for all kanji.\n2. Translate the input into Traditional Chinese (Taiwan). If the input is a word with multiple meanings, list all meanings separated by semicolons.\n3. For words, create three example sentences in Japanese. For sentences, explain key vocabulary or syntax in Traditional Chinese (Taiwan)."
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "仕事"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "{\n  \"furigana\": \"仕事 (しごと)\",\n  \"chinese\": \"工作; 職業; 職務\"\n  \"detail\": [\n    \"仕事が楽しいです。\",\n    \"私は仕事を終えなければなりません。\",\n    \"彼は新しい仕事を見つけました。\"\n  ]\n}"
        }
      ]
    },
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "私は学校に行きます。"
        }
      ]
    },
    {
      "role": "assistant",
      "content": [
        {
          "type": "text",
          "text": "{\n  \"furigana\": \"私(わたし)は学校(がっこう)に行(い)きます。\",\n  \"chinese\": \"我去學校。\",\n  \"detail\": [\n    \"私は: 我，指說話者自己。\",\n    \"学校: 學校，教育機構。\",\n    \"行きます: 去，表示移動到某地。\"\n  ]\n}"
        }
      ]
    }
]

response_format = {
    "type": "json_schema",
    "json_schema": {
        "name": "japanese_translation_schema",
        "strict": True,
        "schema": {
            "type": "object",
            "properties": {
                "furigana": {
                    "type": "string",
                    "description": "The original Japanese word or sentence with furigana for all kanji."
                },
                "chinese": {
                    "type": "string",
                    "description": "Translation of the input into Traditional Chinese, listing multiple meanings separated by semicolons if applicable."
                },
                "detail": {
                    "type": "array",
                    "description": "Example sentences or explanations related to the input.",
                    "items": {
                        "type": "string"
                    }
                }
            },
            "required": [
                "furigana",
                "chinese",
                "detail"
            ],
            "additionalProperties": False
        }
    }
}

class ChatGPT():
    @staticmethod
    def chat(message: str) -> str:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages + [{
                "role": "user",
                "content": message
            }],
            response_format=response_format,
            temperature=1,
            max_completion_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )

        return response.choices[0].message.content
        

