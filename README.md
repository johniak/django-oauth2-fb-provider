django-oauth2-fb-provider
======================

Forked from [django-oauth2-provider](https://github.com/caffeinehit/django-oauth2-provider)



This fork allows you to get access token by "facebook login".

Requirements:
---
* `python-social-auth>=0.1.26`

* `Django>=1.6`


Getting started:
--

<h5>Important: uninstall original *django-oauth2-provider*</h5>

**Add and configure *python-social-auth*** to your project.

**Add apps to django** (names same as in original according to compatibility):

    INSTALLED_APPS = (...
    'provider',
    'provider.oauth2',
    }

**Add urls**:

    url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2'))

Go to the admin panel and **create a new Provider.Client entry**. It will create the client_id and client_secret properties for you.

**Now you can get acces_token by url:**

    /oauth2/access_token/

Parameters are:

* uid - facebook user id
* access_token - facebook api access_token
* grant_type - *facebook*
* client_id - same as in original
* client_secret - same as in original

**Example request:**

    curl -X POST -d "client_id=CLIENT_ID&client_secret=CLIENT_SECRET&grant_type=facebook&uid=FACEBOOK_UID&access_token=FACEBOOK_ACCESS_TOKEN

Help
--

[Documentation of original](http://readthedocs.org/docs/django-oauth2-provider/en/latest/)

[Help of original](https://groups.google.com/d/forum/django-oauth2-provider)

License
=======

*django-oauth2-fb-provider* is released under the MIT License. Please see the LICENSE file for details.
