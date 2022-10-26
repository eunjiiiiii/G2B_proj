#%%
import pandas as pd
from scipy.stats import rankdata
import gower_similarity as go
from pandasgui import show
#%%
df_g = pd.read_csv('./2019공사공고.csv')
df_t1 =pd.read_csv('./2019공사투찰1.csv')
df_t2 =pd.read_csv('./2019공사투찰2.csv')
df_t3 =pd.read_csv('./2019공사투찰3.csv')
df_t4 =pd.read_csv('./2019공사투찰4.csv')
#%%
df_t = pd.concat([df_t1, df_t2, df_t3, df_t4])
#%%
df = pd.read_csv('Final_Gower.csv')
df.drop(axis=1, columns='Unnamed: 0',inplace=True)
#%%
gongo_list=[] #공고에 올라온 변수만 사용하는 과정
for g_element in df_g.columns.tolist():
  for o_element in df.columns.tolist():
    if g_element==o_element:
      gongo_list.append(o_element)
#%%
df = df[gongo_list]
#%%
target_gongo = df.iloc[70000] #test를 위한 sample 공고선택
target_gongo_df = pd.DataFrame(columns= df.columns.tolist())
target_gongo_df.loc[0] = target_gongo
#%%
gomain_df = go.main(df,target_gongo_df,df_g)
#%%
gui = show(gomain_df[['입찰공고번호','공고명','유사도','공사현장','추정금액','추정가격','예정가격','낙찰업체목록내용','낙찰업체투찰률','낙찰업체투찰금액','낙찰하한율']][:-1])
#%%