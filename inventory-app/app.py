from flask import Flask,render_template,request,redirect,url_for,flash
from data_manager import DataManager
app=Flask(__name__)
app.secret_key='your-secret-key-here'
DM=DataManager()
@app.route('/')
def index():
 S=DM.get_summary_stats();RH=DM.get_all_history()[:5]
 return render_template('index.html',stats=S,recent_history=RH)
@app.route('/products')
def products():
 sk=request.args.get('search','')
 if sk:PL=DM.search_products(sk)
 else:PL=DM.get_all_products()
 C=DM.get_categories();return render_template('products.html',products=PL,categories=C,search_keyword=sk)
@app.route('/products/add',methods=['POST'])
def add_product():
 n=request.form.get('name');c=request.form.get('category');q=int(request.form.get('quantity',0));p=float(request.form.get('price',0))
 if n and c:
  pid=DM.add_product(n,c,q,p);flash(f'商品「{n}」を追加しました（ID: {pid}）','success')
 else:flash('商品名とカテゴリは必須です','error')
 return redirect(url_for('products'))
@app.route('/products/<int:product_id>/update',methods=['POST'])
def update_product(product_id):
 a=request.form.get('action');q=int(request.form.get('quantity',0))
 if a=='入庫':qc=q
 elif a=='出庫':qc=-q
 else:flash('無効な操作です','error');return redirect(url_for('products'))
 if DM.update_product_quantity(product_id,qc,a):flash(f'{a}処理が完了しました','success')
 else:flash('在庫更新に失敗しました（在庫不足の可能性があります）','error')
 return redirect(url_for('products'))
@app.route('/history')
def history():
 pid=request.args.get('product_id')
 if pid:
  HL=DM.get_product_history(int(pid));P=DM.get_product_by_id(int(pid));PN=P['name'] if P else '不明'
 else:HL=DM.get_all_history();PN=None
 return render_template('history.html',history=HL,product_name=PN)
@app.template_filter('format_currency')
def format_currency(v):return f'¥{v:,.0f}'
@app.template_filter('format_number')
def format_number(v):return f'{v:,}'
if __name__=='__main__':app.run(debug=True,host='0.0.0.0',port=5001)
