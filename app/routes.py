from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.forms import *
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import *
from flask_login import login_required, login_user, logout_user, current_user
main = Blueprint("main", __name__)


@main.route('/home')
def home():
    return render_template("index.html")


@main.route('/', methods = ['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            hashed_password = generate_password_hash(form.password.data)
            if User.query.filter_by(email = form.email.data).first():
                flash("Email ALready Exist !", "danger")
                return redirect(url_for("main.register"))
            
            if form.password.data != form.confirm_password.data:
                flash("Password is Not Match", "danger")
                return redirect(url_for("main.register"))
            
            user = User(
                username = form.username.data,
                email = form.email.data,
                password = hashed_password
            )
            db.session.add(user)
            db.session.commit()
            flash("Your Account Is Created Successfully", "success")
            return redirect(url_for("main.login"))

    return render_template("register.html", form=form)



@main.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(email = form.email.data).first()
            if user and check_password_hash(user.password, form.password.data):
                login_user(user)
                flash("You Log in Successfully !", "success")
                return redirect(url_for("main.dashboard"))
            else:
                flash("Invalid Credentials", "danger")
    return render_template("login.html", form=form)


@main.route('/logout')
def logout():
    logout_user()
    flash("You Logout Successfully !", "success")
    return redirect(url_for("main.home"))



@main.route('/dashboard')
@login_required
def dashboard():
    jobs = Job.query.filter_by(user_id = current_user.id).order_by(Job.deadline.asc()).all()
    return render_template("dashboard.html", jobs = jobs)



@main.route('/add', methods=['GET', 'POST'])
@login_required
def add_job():
    form = JobForm()
    if form.validate_on_submit():
        job = Job(
            company=form.company.data,
            role=form.role.data,
            link=form.link.data,
            status=form.status.data,
            deadline=form.deadline.data,
            notes=form.notes.data,
            user_id=current_user.id
        )
        db.session.add(job)
        db.session.commit()
        flash('Job added successfully!')
        return redirect(url_for('main.dashboard'))
    return render_template('add_job.html', form=form)



@main.route('/edit/<int:job_id>', methods=['GET', 'POST'])
@login_required
def edit_job(job_id):
    job = Job.query.get_or_404(job_id)
    if job.user_id != current_user.id:
        flash('Unauthorized access')
        return redirect(url_for('dashboard'))
    form = JobForm(obj=job)
    if form.validate_on_submit():
        job.company = form.company.data
        job.role = form.role.data
        job.link = form.link.data
        job.status = form.status.data
        job.deadline = form.deadline.data
        job.notes = form.notes.data
        db.session.commit()
        flash('Job updated!')
        return redirect(url_for('main.dashboard'))
    return render_template('edit_job.html', form=form)



@main.route('/delete/<int:job_id>')
@login_required
def delete_job(job_id):
    job = Job.query.get_or_404(job_id)
    if job.user_id != current_user.id:
        flash('Unauthorized action')
        return redirect(url_for('main.dashboard'))
    db.session.delete(job)
    db.session.commit()
    flash('Job deleted.')
    return redirect(url_for('main.dashboard'))