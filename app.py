from flask import Flask, render_template, request, redirect, url_for, flash
from database import get_db as get_db_menus, init_db as init_db_menus
from database1 import get_db as get_db_orders, init_db as init_db_orders
app = Flask(__name__)
app.secret_key = 'project2026'

items=[]

Menus = [
    {"name":"pizza","price":100},
    {"name":"Burger","price":50},
    {"name":"Sandwich","price":75},
    {"name":"Pasta","price":120},
    {"name":"Vadapav","price":30}
]

@app.route('/')
def home():
    return render_template('home.html',)

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/order', methods=['GET', 'POST'])
def order():
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        quantity  = request.form.get('quantity')

        if not name or not price or not quantity:
            flash('please provide both name ans price','danger')
            return render_template("order.html")
        conn = get_db_orders()
        conn.execute(''' INSERT INTO allorder(name,price,quantity) VALUES(?,?,?)''',
                    (name,price,quantity)
                    )
        
        conn.commit()
        conn.close()

        flash('Order added successfully','success')
        return redirect(url_for('order'))
    
    conn = get_db_orders()
    items = conn.execute('SELECT * FROM allorder').fetchall()
    conn.close()
    return render_template('order.html', items=items)


@app.route("/menu")
def menu():
    conn = get_db_menus()
    menus = conn.execute('SELECT * FROM menus ORDER BY price DESC').fetchall()
    conn.close()
    return render_template('menu.html', menus=menus)

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():
    if request.method == "POST":
        name = request.form.get('name')
        price = request.form.get('price')

        if not name or not price :
            flash('please provide both name ans price','danger')
            return render_template("add_item.html")
        conn = get_db_menus()
        conn.execute(''' INSERT INTO menus(name,price) VALUES(?,?)''',
                    (name,price)
                    )
        
        conn.commit()
        conn.close()
        
        conn =get_db_menus()
        conn.execute('''SELECT * FROM menus 
                     WHERE price = ?''',(price,)).fetchall()
        conn.commit()
        conn.close()

        new_item={"name":name,"price":price}
        Menus.append(new_item)
        flash(f"{name} added successfully","success")
        return redirect(url_for('menu'))
    
    return render_template('add_item.html')

@app.route("/search")
def search():
    q=request.args.get('q','')
    conn = get_db_menus()

    if q:
        menu = conn.execute('''SELECT * FROM menus WHERE 
                                name LIKE ?
                                OR price LIKE ?''',
                                (f'%{q}%', f'%{q}%')).fetchall()
    else:
        menu = conn.execute('SELECT * FROM menus ORDER BY price DESC').fetchall()
    conn.close()
    return render_template("search.html", menus=menu, query=q)
    

if __name__ == "__main__":
    init_db_menus()
    init_db_orders()
    app.run(debug=True)