import pandas as pd
import gower
from scipy.stats import rankdata
def main(df,target_gongo_df,df_g):
  df_final = pd.concat ( [df, target_gongo_df]) #타겟이 dataFrame 형태(한줄)로 들어 온다고 가정
  df_id = df['입찰공고번호'] #공고번호 (key value)
  df_id.loc[-1]= target_gongo_df.입찰공고번호.tolist()[0]
  df_final.drop(axis=1,columns='입찰공고번호',inplace=True) #유사도 예측시 입찰공고번호는 제외
  distance_matrix = gower.gower_matrix(df_final) #gower 라이브러리를 통해 유사도 matrix 도출
  array = distance_matrix[-1] #맨 마지막 df에 target을 붙인 형태이므로 마지막 row 선택
  ranks = rankdata(array)
  df_final['유사도'] = array.tolist()
  df_final['유사도']  = (1 - df_final['유사도']) *100 #유사도를 0~100으로 표현 높을 수록 유사
  df_final['rank'] = ranks.tolist() #target과 가장 가까운 rank 산출(유사도 계수가 낮은 행 선택)
  df_final['입찰공고번호'] = df_id.tolist()
  df_rank_index_df = df_final[(df_final['rank']) < 5].sort_values('rank') # 1,2,3위
  sm = df_rank_index_df[['입찰공고번호','유사도']]
  df_rank_list = df_rank_index_df['입찰공고번호'].tolist()
  df_result = df_g[df_g['입찰공고번호'].isin(df_rank_list)]
  return pd.merge(df_result,sm,how='inner',on='입찰공고번호')