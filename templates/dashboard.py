{% extends "layout.py" %}
{% block body %} 
        <!-- Page Header-->
        <header class="masthead" style="background-image: url('static/assets/img/home-bg.jpg');">
            <div class="container position-relative px-4 px-lg-5">
                <div class="row gx-4 gx-lg-5 justify-content-center">
                    <div class="col-md-10 col-lg-8 col-xl-7">
                        <div class="site-heading">
                            <h1></h1>
                            <span class="subheading"></span>
                        </div>
                    </div>
                </div>
            </div>
        </header>
        {% with messages = get_flashed_messages(with_categories=True) %}
     
        <ul>
          {% for category, message in messages %}
            <li class="alert alert-{{ info }}">{{ message }}</li>
          {% endfor %}
        </ul>
    
    {% endwith %}
   
        <!-- Main Content-->
        <div class="container px-4 px-lg-5">
            <div class="row gx-4 gx-lg-5 justify-content-center">
                <div class="col-md-10 col-lg-8 col-xl-7">
                Hi, {{  session.get('user') }}  

                 
                  <a href="/logout">Logout</a>            
                                    
                    <!-- Divider-->
                    <hr class="my-4" />
                    <!-- Pager-->
                    <div class="d-flex justify-content-end mb-4"><a class="btn btn-primary text-uppercase" href="#!">Older Posts →</a></div>
                    <div class="d-flex justify-content-start mb-4"><a class="btn btn-primary text-uppercase" href="#!">Newer Posts →</a></div>
                </div>
            </div>
        </div>
        
{% endblock %}