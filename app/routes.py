from app import app, db, mail, Message
from flask import render_template, request, flash, redirect, url_for
from app.forms import CustomerInfo, LoginForm
from app.models import User, Product, Cart
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash


@app.route('/')
@app.route('/index')
def index():
    title = "HOME"
    return render_template('index.html', title=title)


@app.route('/login', methods=['GET', 'POST'])
def login():
    title = "Login"
    form = LoginForm()
    if request.method == "POST" and form.validate():
        username = form.username.data
        password = form.password.data
        user = User.query.filter_by(username=username).first()
        if user is None or not check_password_hash(user.password, password):
            flash('Incorrect email/password. Please try again.', 'danger')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        flash('You have successfully logged in!', 'success')
        return redirect(url_for('index'))
    return render_template('login.html', title=title, form=form)

@app.route('/addtocart', methods=['GET', 'POST'])
@login_required
def addtocart():
    if request.method == 'POST':
        name = product.name
        price = product.price
        category = product.category
        description = product.description
        image_url = product.image_url
        new_product_in_cart = Cart(post_title, content, user_id)
        # Add the new post instance to the database
        db.session.add(new_post)
        # Commit
        db.session.commit()
        # Flash a message
        flash('Your post is posted!', 'success')
        # Redirect back to product_detail (we need to specify which product to go back to, 
        # something like product_id = product.id )
        return redirect(url_for('product_detail'))
    return render_template('create_post.html', post=post, title=title)

@app.route('/myinfo')
@login_required
def myinfo():
    title = 'My Info'
    return render_template('myinfo.html', title=title)

@app.route('/mycart', methods=['GET', 'POST'])
def cart():
    title = "CART"
    cart = Cart.query.order_by(Cart.name.desc()).all()
    return render_template('mycart.html', title=title, cart=cart)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    title = "Sign Up"
    form = CustomerInfo()
    if request.method == "POST" and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        phone = form.phone.data
        email = form.email.data
        password = form.password.data
        new_user = User(first_name, last_name, username, phone, email, password)
        db.session.add(new_user)
        db.session.commit()
        msg = Message(f'Hello, {username} - welcome to E-Commerce Site', [email])
        msg.body = 'Welcome to E-Commerce Site! Happy to have you.'
        mail.send(msg)
        flash("You're signed up!", 'success')
        return redirect(url_for('index'))
    return render_template('signup.html', title=title, form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You have successfully logged out", 'primary')
    return redirect(url_for('index'))

@app.route('/myinfo/delete/<int:user_id>', methods=['POST'])
@login_required
def delete_info(user_id):
    user = User.query.get_or_404(user_id)

    if user.id != current_user.id:
        flash("You cannot delete other people")
        return redirect(url_for('myinfo'))
    db.session.delete(user)
    db.session.commit()
    flash("You have been deleted, have a good day!")
    return redirect(url_for('index'))


@app.route('/myinfo/update/<int:user_id>', methods=['GET', 'POST'])
@login_required
def update_info(user_id):
    user = User.query.get_or_404(user_id)
    update_form = CustomerInfo()

    if user.id != current_user.id:
        flash("You cannot update others.")
        return redirect(url_for('myinfo'))
    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        phone = form.phone.data
        email = form.email.data
        password = form.password.data
        address = form.address.data

        db.session.commit()
        flash("You have been updated", 'info')
        return redirect(url_for('index'))
    return render_template('updateinfo.html', form=update_form)