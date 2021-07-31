from flask import Flask, render_template
import os
from . import db


def create_app():
    app = Flask("todolist")
    app.config.from_mapping(
        DATABASE="todos"
    )
        
        
    from . import todolist
    app.register_blueprint(todolist.bp)    
    
    from . import db
    db.init_app(app)
    
    return app
