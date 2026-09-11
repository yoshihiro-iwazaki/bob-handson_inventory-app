import pandas as pd
from datetime import datetime
import os
class DataManager:
 def __init__(self,DD='data'):
  self.DD=DD
  self.pf=os.path.join(DD,'products.csv')
  self.hf=os.path.join(DD,'history.csv')
 def get_all_products(self):
  try:
   DF=pd.read_csv(self.pf)
   return DF.to_dict('records')
  except FileNotFoundError:
   return []
 def get_product_by_id(self,PID):
  DF=pd.read_csv(self.pf);P=DF[DF['id']==int(PID)]
  if not P.empty:return P.iloc[0].to_dict()
  return None
 def search_products(self,kw):
  DF=pd.read_csv(self.pf)
  if kw:
   m=DF['name'].str.contains(kw,case=False,na=False)|DF['category'].str.contains(kw,case=False,na=False)
   DF=DF[m]
  return DF.to_dict('records')
 def add_product(self,n,c,q,p):
  DF=pd.read_csv(self.pf);nid=DF['id'].max()+1 if not DF.empty else 1
  np={'id':nid,'name':n,'category':c,'quantity':q,'price':p,'created_at':datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
  DF=pd.concat([DF,pd.DataFrame([np])],ignore_index=True);DF.to_csv(self.pf,index=False)
  self.add_history(nid,n,'入庫',q,q);return nid
 def update_product_quantity(self,PID,qc,a):
  DF=pd.read_csv(self.pf);idx=DF[DF['id']==int(PID)].index
  if len(idx)==0:return False
  cq=DF.loc[idx[0],'quantity'];nq=cq+qc
  if nq<0:return False
  DF.loc[idx[0],'quantity']=nq;DF.to_csv(self.pf,index=False)
  pn=DF.loc[idx[0],'name'];self.add_history(PID,pn,a,qc,nq);return True
 def get_all_history(self):
  try:
   DF=pd.read_csv(self.hf);DF=DF.sort_values('timestamp',ascending=False);return DF.to_dict('records')
  except FileNotFoundError:return []
 def get_product_history(self,PID):
  DF=pd.read_csv(self.hf);h=DF[DF['product_id']==int(PID)];h=h.sort_values('timestamp',ascending=False);return h.to_dict('records')
 def add_history(self,PID,pn,a,qc,qa):
  DF=pd.read_csv(self.hf);nid=DF['id'].max()+1 if not DF.empty else 1
  nh={'id':nid,'product_id':PID,'product_name':pn,'action':a,'quantity_change':qc,'quantity_after':qa,'timestamp':datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
  DF=pd.concat([DF,pd.DataFrame([nh])],ignore_index=True);DF.to_csv(self.hf,index=False)
 def get_categories(self):
  DF=pd.read_csv(self.pf);return sorted(DF['category'].unique().tolist())
 def get_summary_stats(self):
  DF=pd.read_csv(self.pf);return {'total_products':len(DF),'total_quantity':int(DF['quantity'].sum()),'total_value':float((DF['quantity']*DF['price']).sum()),'categories':len(DF['category'].unique())}
