"""

99. Translation ServerPermalink
Build a demo system, in which the user can translate arbitrary text on the Web browser.

"""



from transformers import pipeline
import pysbd
import streamlit as st
from langdetect import detect


def enja_translator(text):
    seg_en = pysbd.Segmenter(language="en", clean=False)
    translator = pipeline('translation', model='staka/fugumt-en-ja')
    trans = translator(seg_en.segment(text))

    trans_list = [d.get('translation_text') for d in trans]
    trans_text = "".join(trans_list)

    return trans_text

def jaen_translator(text):
    translator = pipeline('translation', model='staka/fugumt-ja-en')
    trans_text = translator(text)[0]['translation_text']

    return trans_text
    

def translator(text):
    if detect(text) == 'en':
        value=enja_translator(text)

    elif detect(text) == 'ja':
        value=jaen_translator(text)

    else:
        value="言語を判定できませんでした。"

    return value    


def main():
    st.title("簡単な英⇔日翻訳")

    input_text = st.text_area("翻訳したい文章を入力してください。", height=300)

    button = st.button("Translate")

    if button:
        trans_txt = translator(input_text)

        st.text_area("翻訳後の文章", trans_txt, height=300)

if __name__ == "__main__":
    main()

