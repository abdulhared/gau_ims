from app import create_app
from app.extensions import celery

app = create_app('development')  # or 'production' based on your environment
app.app_context().push()

if __name__ == '__main__':
    celery.start()    