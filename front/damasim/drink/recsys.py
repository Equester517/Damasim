import pandas as pd
import numpy as np
from django.db import connection
from sklearn.metrics.pairwise import cosine_similarity
#from sklearn.metrics import mean_squared_error # MSE 계산용
#from sqlalchemy.sql.functions import min


def Recsys(dict, recommend_no):

    curs = connection.cursor()
    sqlstr = "SELECT * FROM bev14_prep;"
    curs.execute(sqlstr)
    result = curs.fetchall()

    df = pd.DataFrame(result)

    df.drop(columns=df.columns[0], axis=1, inplace=True)  #앞에 MyUnknownColumn drop

    #df_T = df.transpose()

    #bev_sim = cosine_similarity(df_T, df_T)
    #bev_sim_df = pd.DataFrame(data=bev_sim, index=df.columns, columns=df.columns)

    new_user_id = df.shape[0]

    output_dict = {} # key를 int형으로!!!!
    for key, value in dict.items():
        output_dict[int(key)] = [int(value)]

    new_user_df = pd.DataFrame(data=output_dict, index=[new_user_id], columns=df.columns)
    new_user_df = new_user_df.fillna(0)

    data_ap = df.append(new_user_df, ignore_index=True)

    data_ap_T = data_ap.transpose()
    bev_sim_new = cosine_similarity(data_ap_T, data_ap_T)
    bev_sim_df_new = pd.DataFrame(data=bev_sim_new, index=data_ap.columns, columns=data_ap.columns)

    not_tried_new = get_not_tried_bev(data_ap, new_user_id)

    ratings_pred_new = predict_rating_topsim(data_ap.values, bev_sim_df_new.values, n=20)

    ratings_pred_matrix_new = pd.DataFrame(data=ratings_pred_new, index=data_ap.index,
                                           columns=data_ap.columns)

    recomm_bev_new = recomm_bev_by_userid(ratings_pred_matrix_new, new_user_id, not_tried_new, top_n=recommend_no)

    recomm_bev_new_dict = recomm_bev_new.to_dict() #pd.Series to dict

    #===============정규화 (0~5)
    maxval_dict = max(recomm_bev_new_dict.values())
    minval_dict = min(recomm_bev_new_dict.values())

    for key in recomm_bev_new_dict:
        recomm_bev_new_dict[key] = (recomm_bev_new_dict[key] -minval_dict) / (maxval_dict - minval_dict) * 5

    #print(recomm_bev_new_dict)

    return recomm_bev_new_dict #결과값 dict로 반환

def get_not_tried_bev(ratings_matrix, userId):
    user_rating = ratings_matrix.loc[userId, :]
    tried = user_rating[user_rating>0].index.tolist()
    bev_list = ratings_matrix.columns.tolist()
    not_tried = [bev for bev in bev_list if bev not in tried]

    return not_tried

def predict_rating_topsim(ratings_arr, item_sim_arr, n=20):
    pred = np.zeros(ratings_arr.shape)

    for col in range(ratings_arr.shape[1]):
        top_n_items = [np.argsort(item_sim_arr[:, col])[:-n-1:-1]]
        for row in range(ratings_arr.shape[0]):
            pred[row, col] = item_sim_arr[col,:][top_n_items].dot(
            ratings_arr[row, :][top_n_items].T)
            pred[row, col] /= np.sum(item_sim_arr[col,:][top_n_items])
    return pred

def recomm_bev_by_userid(pred_df, userId, not_tried, top_n):
    recomm_bev = pred_df.loc[userId, not_tried].sort_values(ascending=False)[:top_n]
    return recomm_bev