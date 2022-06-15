import streamlit as st
from PIL import Image
import random
import pandas as pd

subject_id_ls = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113,
                 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126,
                 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213,
                 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226 ]

st.header("第２部ー１")
st.header("確実性等価を求める問題")
st.subheader("")
buttom = st.button('決定')
st.subheader("")

dic = {} 
dic_show = {} 
index = range(1, 53)

if buttom:
     for id, i in zip(subject_id_ls, index):

          question_num = random.randint(1, 17)
          set_num      = random.randint(1, 10)
          set_color_bit    = random.randint(0, 1)

          if set_color_bit == 0:
               set_color = "  緑"
               set_color_en = "Green"
          elif set_color_bit == 1:
               set_color = "  赤"
               set_color_en = "Red"

          #st.header(f"【被験者番号 : {id}】")
          #st.subheader(f"対象問題番号: {question_num}")
          #st.subheader(f"個別くじ番号: {set_num}")
          #st.subheader(set_color)
          #st.subheader("")

          dic_show[i] = [id, question_num, set_num, set_color]
          dic[i] = [id, question_num, set_num, set_color_en]

     show_dict={}
     for k,v in dic_show.items():   # 一度pd.Seriesに変換
          show_dict[k]=pd.Series(v)

     df_show = pd.DataFrame(show_dict).T
     df_show = df_show.rename(columns={0: '被験者番号', 1: '対象問題番号', 2: '個別くじ番号', 3: '色', })
     st.dataframe(df_show, width = 800, height = 2000)

     ## ---------- 回答結果の出力 ---------- ##

     output_dict={}
     for k,v in dic.items():   # 一度pd.Seriesに変換
          output_dict[k]=pd.Series(v)

     df = pd.DataFrame(output_dict).T

     def convert_df(df):
          # IMPORTANT: Cache the conversion to prevent computation on every rerun
          return df.to_csv(index=False).encode('utf-8')

     df = df.rename(columns={0: 'Subject_ID', 1: 'Question number', 2: 'Lottery pair number', 3: 'Color', })

     

     csv = convert_df(df)

     st.download_button(
          label="結果を出力(csv)",
          data=csv,
          file_name= f'Certainty_Equivalence.csv',
          mime='text/csv',
     )
