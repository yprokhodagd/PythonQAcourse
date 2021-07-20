# Book service for GridU course Python for QA 

### How to run application:

1. Install Docker
2. Clone this repository
3. Open terminal and navigate to cloned repository
4. Build docker image:
 > $ docker build -t python-flask-rest .
5. Run container:
 > $ docker run -p 127.0.0.1:5000:5000  python-flask-rest
 
The output will be like
  >GDSpb1331:~ sdronnikova$ docker run -p 127.0.0.1:5000:5000  python-flask-rest
 >* Serving Flask app "books_app.rest_api.flask_api" (lazy loading)
 >* Environment: production
 >  WARNING: This is a development server. Do not use it in a production deployment.
 >  Use a production WSGI server instead.
 >* Debug mode: on
 
 Example of request:
> $ curl http://127.0.0.1:5000/v1/books/latest?limit=1

 
### Run tests with Allure report:
* > pytest --alluredir=my_allure_results
* > allure serve my_allure_results
