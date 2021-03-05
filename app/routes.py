from app import app, db
from flask import render_template, request, flash, redirect, url_for
from app.forms import CustomerInfo, LoginForm
from app.models import User, Cart
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash


@app.route('/')
@app.route('/index')
def index():
    title = "HOME"
    return render_template('index.html', title=title)


@app.route('/login')
def index():
    title = "LOGIN"
    if request.method = "POST" and form.validate():
        username = form.username.data
        password = form.password.data

        flash("You have logged in")
        return redirect(url_for('index'))
    return render_template('login.html', title=title)

@app.route('/mycart')
def index():
    title = "CART"
    cart = Cart.query.order_by(Cart.name.desc()).all)
    return render_template('mycart.html', title=title)

@app.route('/signup')
def index():
    title = "SIGN UP"
    form = CustomerInfo()
    if request.method == "POST" and form.validate():
        first_name = form.first_name.data
        last_name = form.last_name.data
        username = form.username.data
        phone = form.phone.data
        email = form.email.data
        password = form.password.data
        address = form.address.data

        new_user = User(first_name, last_name, username, phone, email, password, address)
        db.session.add(new_user)

        flash("You have been created")
        return redirect(url_for('index'))

    return render_template('signup.html', title=title form=form)


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


@app.route('/myinfo/update/<int:user_id', methods=['GET', 'POST'])
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