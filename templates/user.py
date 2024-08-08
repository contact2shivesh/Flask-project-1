{% extends "layout.py" %}
{% block body %} 

 <!-- Page Header-->
    <header class="masthead" style="background-image: url('assets/img/contact-bg.jpg')">
        <div class="container position-relative px-4 px-lg-5">
            <div class="row gx-4 gx-lg-5 justify-content-center">
                <div class="col-md-10 col-lg-8 col-xl-7">
                    <div class="page-heading">
                        <h1>User</h1>
                    </div>
                </div>
            </div>
        </div>
    </header>
    
<div style="width:400px;margin:20px 0px 200px 200px;">
    <form id="userForm" name="userForm" action = "/user" method="post" novalidate data-sb-form-api-token="API_TOKEN">
        <div class="form-floating"  style="margin-bottom:20px;">
            <input class="form-control" id="userName" name="userName" type="text" placeholder="Enter your name..." data-sb-validations="required" />
            <label for="name">Name</label>
            <div class="invalid-feedback" data-sb-feedback="name:required">A name is required.</div>
        </div>      
        <button class="btn btn-primary text-uppercase" id="submitButton" type="submit">Send</button>
    </form>
</div>    

{% endblock %}