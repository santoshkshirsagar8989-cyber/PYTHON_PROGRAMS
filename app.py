from flask import Flask, render_template, request, redirect, session, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from database import get_db as get_db_menus, init_db as init_db_menus
from database1 import get_db as get_db_orders, init_db as init_db_orders
from userdatabase import get_db as get_db_user, init_db as init_db_user
app = Flask(__name__)
app.secret_key = 'project2026'

items=[]

Menus = [
    { "SELECT * FROM menus ORDER BY price DESC" }
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
    if 'name' not in session:
        flash(f"please login first", 'danger')
        return redirect(url_for('login'))

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
    if session.get('role') != 'employee':
        flash(f"only for employee,You can use order to buy items ", 'danger')
        return redirect(url_for('login'))
    
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



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username'].strip()
        password = request.form['password']
        
        conn = get_db_user()
        # Check if username already exists
        existing = conn.execute('SELECT * FROM userinfo WHERE name = ?', (username,)).fetchone()
        if existing:
            flash('Username already exists!', 'danger')
            conn.close()
            return render_template('register.html')
        
        hashed = generate_password_hash(password)
        conn.execute('INSERT INTO userinfo (name, password) VALUES (?, ?)', (username, hashed))
        conn.commit()
        conn.close()
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template("register.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('username', '').strip()
        password = request.form.get('password', '')

        if not name or not password:
            flash('Please enter both username and password.', 'danger')
            return render_template('login.html')
        
        conn = get_db_user()
        user = conn.execute('SELECT id, name, password, role FROM userinfo WHERE name = ?', (name,)).fetchone()
        conn.close()
        
        if user and check_password_hash(user['password'], password):
            session['name'] = name
            session['role'] = user['role'] if user['role'] else 'customer'
            flash(f'Welcome {name}!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html')

@app.route('/logout')
def logout():
    
    session.pop('name', None)
    session.pop('role', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('home'))

@app.route('/beverages')
def beverages():
    conn = get_db_menus()
    rows = conn.execute('''SELECT beverages.name AS beverage_name, COUNT(menus.id) AS beverage_count
                         FROM beverages
                         LEFT JOIN menus ON beverages.name = menus.name
                         GROUP BY beverages.name
                         ORDER BY beverages.name ''').fetchall()
    conn.close()
    return render_template("beverages.html", rows=rows)

if __name__ == "__main__":
    init_db_menus()
    init_db_orders()
    init_db_user()
    app.run(debug=True)