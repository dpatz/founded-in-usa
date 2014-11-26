import os

from flask import Flask, render_template
from flask.ext import admin, login

from flask_debugtoolbar import DebugToolbarExtension

from werkzeug.contrib.fixers import ProxyFix

from app.models import db, User, Company, Pair
from app.views import AdminIndexView, CompanyView, TypeformView

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

toolbar = DebugToolbarExtension(app)
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

# handle the proxy headers set in the Nginx configuration
app.wsgi_app = ProxyFix(app.wsgi_app)

db.app = app
db.init_app(app)


# Initialize flask-login
def init_login():
    login_manager = login.LoginManager()
    login_manager.init_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)


@app.route('/')
def index():
    entries = Company.query.\
                    with_entities(Company.name, Company.url, Company.logo).\
                    filter_by(status='accepted').\
                    order_by(Company.name).all()
    companies = [dict(name=row[0], url=row[1], logo=row[2]) for row in entries]

    return render_template('index.html', companies=companies)


@app.route('/about')
def about():
    return render_template('about.html')


# Google WebMaster Tools verification page
@app.route("/google25e87b64455912d9.html")
def site_verification():
    """Returns site verification content"""
    return app.send_static_file("site_verification.html")


# Robots file
@app.route("/robots.txt")
def robots_txt():
    return app.send_static_file("robots.txt")

@app.route("/sitemap.xml")
def sitemap_xml():
    return app.send_static_file("sitemap.xml")


# Initialize flask-login
init_login()

# Create admin
admin = admin.Admin(app, 'Admin', index_view=AdminIndexView(), base_template='layout.html')

# Add Companies view
admin.add_view(CompanyView(Company, db.session, name='Companies', endpoint="companies"))
admin.add_view(TypeformView(name='Get Typeform new entries', endpoint="data"))
