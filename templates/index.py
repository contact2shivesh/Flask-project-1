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
        <!-- Main Content-->
        <div class="container px-4 px-lg-5">
            <div class="row gx-4 gx-lg-5 justify-content-center">
                <div class="col-md-10 col-lg-8 col-xl-7">
                {% for post in posts %}                              
                    <!-- Post preview-->
                    <div class="post-preview">
                        <a href="/post/{{post.slug}}">
                            <h2 class="post-title">{{ post.title }}</h2>
                            <h3 class="post-subtitle">{{ post.tagline }}</h3>
                        </a>
                        <p class="post-meta">
                            Posted by
                            <a href="#!">{{params['headName']}}</a>
                            on {{ post.date }}
                        </p>
                    </div> 
                    {{post.content[0:143]}}
                    {% endfor %}                            
                    <!-- Divider-->
                    <hr class="my-4" />
                    <!-- Pager-->
                    <div class="d-flex justify-content-end mb-4"><a class="btn btn-primary text-uppercase" href="#!">Older Posts →</a></div>
                    <div class="d-flex justify-content-start mb-4"><a class="btn btn-primary text-uppercase" href="#!">Newer Posts →</a></div>
                </div>
            </div>
        </div>
        
{% endblock %}