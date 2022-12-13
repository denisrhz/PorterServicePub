from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms import MessageForm
from app.models import Service, Message, City

@app.route('/')
@app.route('/index')
def index():
    services = Service.query.all()
    return render_template('index.html', services=services)

@app.route('/message/<service>', methods=['GET', 'POST'])
def message(service):
    service = Service.query.filter_by(slug=service).first_or_404()
    form = MessageForm()
    form.city.choices = [(record.id, record.name) for record in City.query.all()]
    if form.validate_on_submit():
        message = Message(author=form.author.data,
                            phone=form.phone.data,
                            body=form.body.data,
                            service_id=service.id,
                            city_id=form.city.data)
        db.session.add(message)
        db.session.commit()
        return redirect(url_for('message', service=service.slug))
    return render_template('message.html', form=form)

